# coding: utf-8


"""Small and simple gravatar generator.

Usage
=====

Initialize
----------

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False
                       )

In template
-----------

With default parameters:

    {{ 'zzz.sochi@gmail' | gravatar }}

Bigger and adult:

    {{ 'zzz.sochi@gmail' | gravatar(size=200, default='x') }}

Patameters
----------

All parameters described in http://gravatar.com/site/implement/images/.


API
---

.. py:class:: Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False,
                       )

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

    .. py:method:: __call__(email, **kw)

        Build gravatar link.

        :param email: Email for create link
        :param kw: Reload defaults

    Default parameters. May runtime changed.

    .. py:attribute:: size
    .. py:attribute:: rating
    .. py:attribute:: default
    .. py:attribute:: force_default
    .. py:attribute:: force_lower

"""

from setuptools import setup
from distutils.core import setup

# python setup.py bdist_egg
# python setup.py sdist --formats=bztar


setup(
        name = 'Flask-Gravatar',
        version = '0.2',
        license='BSD',
        description = 'Small extension to make using gravatar easy',
        long_description = __doc__,
        author = 'Zelenyak Aleksandr aka ZZZ',
        author_email = 'zzz.sochi@gmail.com',
        url = 'http://www.python.org/pypi/Flask-Gravatar/',
        platforms = 'any',

        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],

        install_requires = ['Flask'],

        packages = ['flaskext'],
        namespace_packages = ['flaskext'],
)



