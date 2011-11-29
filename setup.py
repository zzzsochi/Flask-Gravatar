# coding: utf-8

from setuptools import setup
from distutils.core import setup

setup(
        name = 'Flask-Gravatar',
        version = '0.2.3',
        license='BSD',
        description = 'Small extension for Flask to make using Gravatar easy',
        long_description = open('README.rst').read(),
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



