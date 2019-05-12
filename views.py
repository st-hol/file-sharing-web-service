from flask import Blueprint, render_template, request, redirect, url_for, send_file, abort, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from io import BytesIO

from datetime import datetime
from datetime import timedelta


from . import db
from .models import User, FileContents

from .utility import calc_remaining_lifetime, delete_expired_files
from .account_forms import LoginForm, RegisterForm
main = Blueprint('main', __name__)


from . import create_app

@main.route('/', methods=['POST', 'GET'])
def index():
    db.create_all(app=create_app())
    return render_template('index.html')



@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember = form.remember.data)
                return redirect(url_for('main.dashboard'))

        return render_template('common/fail.html')

    return render_template('guest/login.html', form=form)


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('common/success.html')

    return render_template('guest/signup.html', form=form)



@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@main.route('/upload-form', methods=['POST', 'GET'])
def upload_form():
    return render_template('user/upload-form.html')


@main.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    life_minutes = float(request.form['inputMinutes'])
    exp_time = datetime.now() + timedelta(minutes = life_minutes)

    if current_user.is_anonymous:
        author_id = -1
    else:
        author_id = current_user.id

    new_file = FileContents(name=file.filename, data=file.read(), expiration_time=exp_time, author_id=author_id)
    db.session.add(new_file)
    db.session.commit()

    #return render_template('success.html')
    if new_file:
        return jsonify({'id': new_file.id})
    return jsonify({'error': 'some error!'})



@main.route('/download/<int:id_file>')
def download(id_file):
    file_to_download = FileContents.query.filter_by(id = id_file).first()
    return send_file(BytesIO(file_to_download.data), attachment_filename = file_to_download.name, as_attachment = True)

@main.route('/show-all')
def show_all():

    delete_expired_files()

    if current_user.is_anonymous:
        author_id = -1
        template = 'guest/files-list.html'
    else:
        template = 'user/show-all.html'
        author_id = current_user.id

    all_files = FileContents.query.filter_by(author_id=author_id).all()
    #all_files = FileContents.query.all()

    return render_template(template, all_files=all_files)

@main.route('/show-single', methods=['POST', 'GET'])
def show_single():

    delete_expired_files()

    id_file = int(request.form['idFile'])
    searched_file = FileContents.query.filter_by(id=id_file).first()
    if searched_file:
       # from utility import calc_remaining_lifetime
        return render_template('common/show-single.html', file=searched_file,
                               remaining_lifetime=calc_remaining_lifetime(searched_file.expiration_time))
    else:
        abort(404) # not-found


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html', name=current_user.username)



