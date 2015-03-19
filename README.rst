==============
Flask Gravatar
==============

This is small and simple integration `gravatar`_ into `flask`_.

.. _flask: http://flask.pocoo.org
.. _gravatar: http://gravatar.com

Installation
------------

Install the extension with one of the following commands:
::

    $ easy_install Flask-Gravatar

or alternatively if you have pip installed:
::

    $ pip install Flask-Gravatar

How to Use
----------

Initialize with flask application and default parameters:
::

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        use_ssl=False,
                        base_url=None)

Then in your template:
::

    {{ 'zzz.sochi@gmail.com' | gravatar }}

Bigger and adult:
::

    {{ 'zzz.sochi@gmail.com' | gravatar(size=200, rating='x') }}

Parameters
~~~~~~~~~~

All parameters are described in `gravatar documentation`_.

.. _gravatar documentation:  http://gravatar.com/site/implement/images


.. include:: ../CHANGELOG
