Rate Social
===========

This is the backend for our new Social Rating app.

### Getting Started
Clone the repo

```
git clone https://github.com/zconnelly13/rate-social
```

Change your port number in rate\_people/settings.py in the DATABASES dict

Syncdb to create the database file (db.sqllite3) in the project's root directory

```
python manage.py syncdb
```

Runserver

```
python manage.py runserver 0.0.0.0:[your port number]
```

Now open up a web browser and go to ```/admin``` to see all of the tables you just created
To add new users / new ratings with a GET request see the ```database/views.py``` file 

TODO: Insert Example Request
