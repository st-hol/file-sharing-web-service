from datetime import datetime
from .models import FileContents


def calc_remaining_lifetime(expiration_time):
    expiration_time = datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f')
    remaining = expiration_time - datetime.now()
    return remaining


def delete_expired_files():
    FileContents.query.filter(FileContents.expiration_time <= datetime.now()).delete()
