================
 Flask-Gravatar
================

.. currentmodule:: flask_gravatar

.. raw:: html

    <p style="height:22px; margin:0 0 0 2em; float:right">
        <a href="https://travis-ci.org/zzzsochi/flask-gravatar">
            <img src="https://travis-ci.org/zzzsochi/flask-gravatar.png?branch=master"
                 alt="travis-ci badge"/>
        </a>
        <a href="https://coveralls.io/r/zzzsochi/flask-gravatar">
            <img src="https://coveralls.io/repos/zzzsochi/flask-gravatar/badge.png?branch=master"
                 alt="coveralls.io badge"/>
        </a>
    </p>

This is small and simple integration `gravatar`_ into `flask`_.

.. _flask: http://flask.pocoo.org
.. _gravatar: http://gravatar.com

Contents
--------

.. contents::
   :local:
   :depth: 1
   :backlinks: none


.. _installation:

Installation
============

Flask-Gravatar is on PyPI so all you need is:

.. code-block:: console

    $ pip install Flask-Gravatar

The development version can be downloaded from `its page at GitHub
<http://github.com/zzzsochi/flask-gravatar>`_.

.. code-block:: console

    $ git clone https://github.com/zzzsochi/flask-gravatar.git
    $ cd flask-gravatar
    $ python setup.py develop
    $ ./run-tests.sh

.. _usage:

Usage
=====

Initialize with flask application and default parameters:

.. code-block:: python

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False,
                        use_ssl=False,
                        base_url=None)

Alternatively, the default parameters can be read from the application
config values in `GRAVATAR_SIZE`, `GRAVATAR_RATING`, `GRAVATAR_DEFAULT`,
`GRAVATAR_FORCE_DEFAULT`, `GRAVATAR_FORCE_LOWER`, `GRAVATAR_USE_SSL`,
and `GRAVATAR_BASE_URL`.

Then in your template:

.. code-block:: jinja

    {{ 'zzz.sochi@gmail.com' | gravatar }}

Bigger and adult:

.. code-block:: jinja

    {{ 'zzz.sochi@gmail.com' | gravatar(size=200, rating='x') }}

Parameters
----------

All parameters are described in `gravatar documentation`_.

.. _gravatar documentation:  http://gravatar.com/site/implement/images

.. _api:

API
===

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


.. include:: ../CHANGES.rst

.. include:: ../CONTRIBUTING.rst

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
