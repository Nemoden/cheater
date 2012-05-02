Cheater
===

This is a [Python](http://www.python.org/) web application written with 
[Flask](http://flask.pocoo.org/), 
[SQLAlchemy](http://www.sqlalchemy.org/) and 
[WTForms](http://wtforms.simplecodes.com/docs/dev/)

This is a "beta than nothin'" developed within 3 days,
so some some stuff maybe does not work at all 
or does not work as it was expected :)

Intent
---

Write a simple cheatsheets storage.
Sometimes I come across interesting articles I want to conspect for myself
or I run into a problem I resolve and want to keep the solution somewhere...
All in all, who can manage all the stuff inside a head? So, basically `Cheater`
helps to keep notes

### Run on localhost

Create database called `cheater` (for mysql):

```sql
create database `cheater`;
```

change the database DSN in `cheater.database` to whatever you have

#### Create tables

```python
python manage.py db --create-all
```

#### Run server on localhost

```python
python manage.py runserver [port] [-d | --debug ]
```

Navigate to 127.0.0.1:port in your browser. The default [Werkzeug](http://werkzeug.pocoo.org/) (used by the application) port is 5000,
so if you run

```
python manage.py runserver
```

it will run on 127.0.0.1:5000


There is a bunch of stuff yet to todo here:

- auth with OpenID, store and verify identity with [Flask-Principal](http://packages.python.org/Flask-Principal/)
- allow cheat name change (the app reconizes cheat by it's name or by name's slug to be precise)
- use `deferred` on some SQLAlchemy declarative based fields
- add some tests
- add some features to the application
- add some features to the manage.py
- add some js
- add some navigation
- fix some templates
- fix some css
- fix some bugs

[Wheee](http://cheater.nemoden.com/)
