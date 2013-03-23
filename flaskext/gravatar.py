# coding: utf8

import hashlib

from flask import _request_ctx_stack

try:
    from flask import _app_ctx_stack
except ImportError:
    _app_ctx_stack = None

# Which stack should we use? _app_ctx_stack is new in 0.9
connection_stack = _app_ctx_stack or _request_ctx_stack


class Gravatar(object):
    """Simple object for create gravatar link.

        gravatar = Gravatar(app,
                            size=100,
                            rating='g',
                            default='retro',
                            force_default=False,
                            force_lower=False,
                            use_ssl=False
                           )

    :param app: Your Flask app instance
    :param size: Default size for avatar
    :param rating: Default rating
    :param default: Default type for unregistred emails
    :param force_default: Build only default avatars
    :param force_lower: Make email.lower() before build link
    :param use_ssl: Use https rather than http
    """

    def __init__(self, app=None, size=100, rating='g', default='retro',
                 force_default=False, force_lower=False, use_ssl=False, **kwargs):

        self.size = size
        self.rating = rating
        self.default = default
        self.force_default = force_default
        self.force_lower = force_lower
        self.use_ssl = use_ssl

        self.app = None

        if app is not None:
            self.init_app(app, **kwargs)

    def get_app(self, reference_app=None):
        """Helper method that implements the logic to look up an application."""

        if reference_app is not None:
            return reference_app

        if self.app is not None:
            return self.app

        ctx = connection_stack.top

        if ctx is not None:
            return ctx.app

        raise RuntimeError('Application not registered on Gravatar'
                           ' instance and no application bound'
                           ' to current context')

    def init_app(self, app):
        """Initializes the Flask-Gravata extension for the specified application.

        :param app: The application.
        """

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.jinja_env.filters.setdefault('gravatar', self)
        app.extensions['gravatar'] = self

    def __call__(self, email, size=None, rating=None, default=None,
                 force_default=None, force_lower=False, use_ssl=None):

        """Build gravatar link."""

        if size is None:
            size = self.size

        if rating is None:
            rating = self.rating

        if default is None:
            default = self.default

        if force_default is None:
            force_default = self.force_default

        if force_lower is None:
            force_lower = self.force_lower

        if force_lower:
            email = email.lower()

        if use_ssl is None:
            use_ssl = self.use_ssl

        if use_ssl:
            url = 'https://secure.gravatar.com/avatar/'
        else:
            url = 'http://www.gravatar.com/avatar/'

        hash = hashlib.md5(email).hexdigest()

        link = '{url}{hash}'\
               '?s={size}&d={default}&r={rating}'.format(**locals())

        if force_default:
            link = link + '&f=y'

        return link
