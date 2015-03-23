# -*- coding: utf-8 -*-
#
# This file is part of Flask-Gravatar
# Copyright (C) 2015 CERN.
#
# Flask-Gravatar is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""General unit tests."""

import sys

from unittest import TestCase

from flask import Flask

from flask_gravatar import Gravatar

# PY2/3 compatibility
if sys.version_info[0] == 3:
    def b(s):
        return s.encode("latin-1")
else:
    def b(s):
        return s


class FlaskTestCase(TestCase):

    """Mix-in class for creating the Flask application."""

    def setUp(self):
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.logger.disabled = True
        self.app = app

    def tearDown(self):
        self.app = None


class TestGravatar(FlaskTestCase):

    def test_constructor(self):
        Gravatar(self.app)

    def test_init_app(self):
        gravatar = Gravatar()
        if hasattr(self.app, 'extensions'):
            del self.app.extensions
        gravatar.init_app(self.app)

    def test_extension_call(self):
        gravatar = Gravatar(self.app)
        link = gravatar('email@example.com', use_ssl=True)
        assert link == ('https://secure.gravatar.com/avatar/'
                        '5658ffccee7f0ebfda2b226238b1eb6e?s=100&d=retro&r=g')

        link = gravatar('email@example.com')
        assert link == ('http://www.gravatar.com/avatar/'
                        '5658ffccee7f0ebfda2b226238b1eb6e?s=100&d=retro&r=g')

        link = gravatar('email@example.com', base_url='http://example.com/')
        assert link == ('http://example.com/avatar/'
                        '5658ffccee7f0ebfda2b226238b1eb6e?s=100&d=retro&r=g')

        link = gravatar('email@example.com', force_default=True)
        assert '&f=y' in link

    def test_secure_request(self):
        gravatar = Gravatar(self.app)

        @self.app.route('/<email>')
        def index(email):
            return gravatar(email)

        client = self.app.test_client()
        response = client.get('/email@example.com',
                              base_url='https://localhost')
        secure_link = gravatar('email@example.com', use_ssl=True)
        assert b(secure_link) == response.data

    def test_parameters(self):
        gravatar = Gravatar(self.app, force_lower=True)
        assert gravatar('email@example.com') == gravatar('Email@EXAMPLE.com',
                                                         force_lower=None)
