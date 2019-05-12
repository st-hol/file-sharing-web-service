# file-sharing-web-service


Веб-сервис файлообменник.

На главной странице:
  1) меню(регистрация, вход, личный кабинет)
  2) форма загрузки файлов: просит файл и время его жизни в минутах
  3) кнопка "show all": показать все доступные файлы (для анонимного и авторизированного юзера отображает разное: для анонимов файлы общие, для авторизированного юзера - персональные)
 ___________________________________________________________________________________________________________________
Неавторизированные пользователи(гости) могут загружать файлы и скачивать их, доступ к этим файлам - общий.
Авторизированный пользователь загружает файлы под собственным ID, т.е. его файлы доступны только ему.
На странице просмотра файлов есть форма "inspect file by id". Позволяет узнать, сколько осталось жить файлу с конкретным id.
___________________________________________________________________________________________________________________

Развернутый на хероку: https://file-sharing-web-service.herokuapp.com/

ВНИМАНИЕ: фича!хотя скорее, все же баг. при загрузке файлов, размер которых меньше приблизительно 1кБ всё ок, больше 1кб - heroku выдает "application error", хотя файл все же загружает. на локальном такого не было =/

//todo пофиксить

___________________________________________________________________________________________________________________
Запуск на локальной машине:
  > cd [директория с проектом]
  
  > virtualenv env
  
  > env\Scripts\activate
  
  > pip install -r requirements.txt
  
  > FLASK_APP=[директория с проектом]
  
  > flask run
