# Market
market in Django

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AmiirEbadi/Market.git
$ cd Market
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

At this step you should make migrations to database:

```sh
(venv)$ python manage.py makemigration
(venv)$ python manage.py migrate
```

Once making the migrations has finished:

```sh
(venv)$ python manage.py runserver
```
