Welcome to Flask Gravatar's documentation!
==========================================

.. module:: flask_gravatar

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
                        force_lower=False,
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


API Reference
-------------

.. class:: flask_gravatar.Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False)

    Simple object for create gravatar link.

    :param app: Your Flask app instance
    :type app: flask.Flask
    :param size: Default size for avatar
    :type size: int
    :type size: str
    :param rating: Default rating
    :type rating: str
    :param default: Default type for unregistred emails
    :type default: str
    :param force_default: Build only default avatars
    :type force_default: bool
    :param force_lower: Make email.lower() before build link
    :type force_lower: bool

    .. method:: __call__(email, \*\*kw)

        Build gravatar link.

        :param email: Email for create link
        :param kw: Reload defaults

    Default parameters. May change in runtime.

    .. attribute:: size
    .. attribute:: rating
    .. attribute:: default
    .. attribute:: force_default
    .. attribute:: force_lower


.. include:: ../CHANGELOG
