# file-sharing-web-service


Веб-сервис файлообменник.

На главной странице:
  1) меню(регистрация, вход, личный кабинет)
  2) форма загрузки файлов: просит файл и время его жизни в минутах
  3) кнопка "show all": показать все доступные файлы (для анонимного и авторизированного юзера отображает разное: для анонимов файлы общие, для авторизированного юзера - персональные)
 
Неавторизированные пользователи(гости) могут загружать файлы и скачивать их, доступ к этим файлам - общий.
Авторизированный пользователь загружает файлы под собственным ID, т.е. его файлы доступны только ему.
На странице просмотра файлов есть форма "inspect file by id". Позволяет узнать, сколько осталось жить файлу с конкретным id.


Развернутый на хероку: https://web-service-file-exchanger.herokuapp.com/ 


Запуск на локальной машине:
  > cd [директория с проектом]
  > virtualenv env
  > env\Scripts\activate
  > pip install -r requirements.txt
  > FLASK_APP=[директория с проектом]
  > flask run
