# -*- coding: utf-8 -*-
#
# This file is part of Flask-Gravatar
# Copyright (C) 2015 CERN.
#
# Flask-Gravatar is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""General unit tests."""

from unittest import TestCase

from flask import Flask

from flask_gravatar import Gravatar


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
        gravatar.init_app(self.app)
