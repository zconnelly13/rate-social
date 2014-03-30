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

To Add a User:
```
http://localhost:1313/addUser/?name=Doge&profile_picture_url=http%3A//static02.mediaite.com/geekosystem/uploads/2013/12/doge.jpg
```

To Add a Rating: (note that the rater and ratee parameters are id's for their respective User objects)

```
http://localhost:1313/addRating/?rater=1&ratee=2&comment=wowmuchdjango&number=10.0
```
