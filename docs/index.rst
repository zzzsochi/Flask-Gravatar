
Welcome to Flask Gravatar's documentation!
==========================================

.. module:: flaskext.gravatar

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

.. class:: flaskext.gravatar.Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False)

    Simple object for create gravatar link.

    :param app: Your Flask app instance
    :type app: flask.Flask
    :param size: Default size for avatar
    :type size: int or str
    :param rating: Default rating
    :type rating: str
    :param default: Default type for unregistred emails
    :type default: str
    :param force_default: Build only default avatars
    :type force_default: bool
    :param force_lower: Make email.lower() before build link
    :type force_lower: bool

    .. method:: __call__(email, **kw)

        Build gravatar link.

        :param email: Email for create link
        :param kw: Reload defaults

    Default parameters. May change in runtime.

    .. attribute:: size
    .. attribute:: rating
    .. attribute:: default
    .. attribute:: force_default
    .. attribute:: force_lower


Changelog
---------

0.4.1 2013-11-07
~~~~~~~~~~~~~~~~

* Python 3 support (pull #9)


0.4.0 2013-08-09
~~~~~~~~~~~~~~~~

* Add custom url support (pull #7)
* Use setuptools (pull #6)

0.3.0 2013-03-23
~~~~~~~~~~~~~~~~

* Enable registering multiple times in one process

0.2.4 2012-11-28
~~~~~~~~~~~~~~~~

* Add init_app method
* Some bugs fixes

0.2.3 2011-11-29
~~~~~~~~~~~~~~~~

* Add HTTPS suppport

0.2.2 2011-01-10
~~~~~~~~~~~~~~~~

* First public release
* It's work

