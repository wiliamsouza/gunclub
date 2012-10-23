.. image:: https://raw.github.com/wiliamsouza/gunclub/master/gunclub/static/img/gunclub290x52.png

Gunclub provides a management software for small gun club.

Status
------

.. image:: https://travis-ci.org/wiliamsouza/gunclub.png

License
-------

Gunclub is distributed under the terms of the Apache License, Version 2.0.
The full terms and conditions of this license are detailed in the LICENSE file.


Quick start
-----------

At this stage gunclub is only suitable for developers who want to contribute
but you have an interest on use it to manage your gun club let me know
sending a mail to wiliamsouza83@gmail.com.

Start cloning the repo::

    git clone git://github.com/wiliamsouza/gunclub.git

Create a virtual environment::

    virtualenv gunclub

Activate virtual environment::

    cd gunclub
    source bin/activate
    pip install -r requirements.txt 

Running unit tests::

    cd gunclub
    python manage.py tests

Configure local development settings::

    cp gunclub/development_settings.py.example gunclub/development_settings.py

Sync database::

    python manage.py syndb

Running Django development server::

    python manage.py runserver

You'll see the following output on the command line::

    Validating models...
    0 errors found.

    Django version 1.4, using settings 'mysite.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Point your browser to http://127.0.0.1:8000/.

