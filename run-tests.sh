#!/bin/sh
#
# This file is part of Flask-Gravatar
# Copyright (C) 2015 CERN.
# Copyright (C) 2018 Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Flask-Gravatar is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

pydocstyle flask_gravatar tests && \
isort -rc -c -df flask_gravatar && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
