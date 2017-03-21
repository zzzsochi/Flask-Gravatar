================
 Flask Gravatar
================

.. image:: https://img.shields.io/travis/zzzsochi/Flask-Gravatar.svg
        :target: https://travis-ci.org/zzzsochi/Flask-Gravatar

.. image:: https://img.shields.io/coveralls/zzzsochi/Flask-Gravatar.svg
        :target: https://coveralls.io/r/zzzsochi/Flask-Gravatar

.. image:: https://img.shields.io/github/tag/zzzsochi/Flask-Gravatar.svg
        :target: https://github.com/zzzsochi/Flask-Gravatar/releases

.. image:: https://img.shields.io/pypi/dm/Flask-Gravatar.svg
        :target: https://pypi.python.org/pypi/Flask-Gravatar

.. image:: https://img.shields.io/github/license/zzzsochi/Flask-Gravatar.svg
        :target: https://github.com/zzzsochi/Flask-Gravatar/blob/master/LICENSE

About
=====

This is small and simple integration `gravatar`_ into `flask`_.

.. _flask: http://flask.pocoo.org
.. _gravatar: http://gravatar.com

Installation
============

Flask-Gravatar is on PyPI so all you need is: ::

    pip install Flask-Gravatar

Documentation
=============

Initialize with flask application and default parameters: ::

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        use_ssl=False,
                        base_url=None)

Then in your template: ::

    {{ 'zzz.sochi@gmail.com' | gravatar }}

Bigger and adult: ::

    {{ 'zzz.sochi@gmail.com' | gravatar(size=200, rating='x') }}

Parameters
----------

All parameters are described in `gravatar documentation`_.

.. _gravatar documentation:  http://gravatar.com/site/implement/images

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also show code coverage: ::

    ./run-tests.sh
