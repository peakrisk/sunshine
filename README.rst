===============================
Sunshine
===============================

Rain or shine, weather data repository.

A simple web application to store data from Personal Weather Stations.

It provides a simple REST API.

Also provides an API to allow querying and retrieval of data.


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export SUNSHINE_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/swfiua/sunshine
    cd sunshine
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server


pip install woes
----------------

I had trouble the *pip install* and got this error due to missing cffi
headers I think:

::

    c/_cffi_backend.c:13:17: fatal error: ffi.h: No such file or directory


On Ubuntu, I fixed this with: 
    
.. code-block:: bash

   sudo apt-get install libffi-dev

Reminds me one reason I like Arch linux:
   
   is the dev packages are partof the library too.  They are tiny and
   so including the headers saves a lot of hassle it little cost.

Deployment
----------

In your production environment, make sure the ``SUNSHINE_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
