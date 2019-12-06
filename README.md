pip install -r requirements.txt

./manage.py migrate

./manage.py createsuperuser

./manage.py runserver

URL AUTHENTICATION JWT: "/api/token/" param {"username": "admin", "password": "testpass"}
Authorization format:"Authorization: Bearer 123456789testtoken123456789" 
