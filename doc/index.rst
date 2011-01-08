Small and simple gravatar generator.

Usage
=====

Initialize
----------

    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False)

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

.. class:: Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False)

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

    Default parameters. May runtime changed.

    .. attribute:: size
    .. attribute:: rating
    .. attribute:: default
    .. attribute:: force_default
    .. attribute:: force_lower


