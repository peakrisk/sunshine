Goal
====

For now the aim is to create something I can run at home to load data
from my own simple raspberry pi weather station.

I only have pressure, humitity and temperature at the moment.

It would be good to know other fields I should add to observations:

https://github.com/peakrisk/sunshine/blob/master/sunshine/rays/models.py#L29

Once I have something working I'll be aiming to host it somewhere local.

Story so far
============

I started with *cookiecutter-flask*:

https://github.com/sloria/cookiecutter-flask

This gave me a lot of boilerplate and hints at how to use Flask. So
far, so good.

Javascript
==========

I am trying not to hate this too much, but the security side of it
scares me.  

For example, there is this horror story:

http://flask.pocoo.org/docs/0.10/security/#json-security

Uploading observations
======================

I will create a python module to talk to the webservice.

With that we should be able to just do:

   data = readings()
   flask.save(data)

And you will just need to write the readings() function that returns
either a list of dictionaries with the readings to save.

Now there will be some config, such as your weather station ID and url
to find the *sunshine* repository.

I'm also going to add an interpret function to the flask thing, that
will take data and return what it is able to extract from it.  I figure
this will be handy debugging new readings() scripts.


Making a swagger documented REST api
====================================

http://flask-restplus.readthedocs.org/en/latest/

Working with karma pi
=====================
