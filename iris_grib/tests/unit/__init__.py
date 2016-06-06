# (C) British Crown Copyright 2013 - 2016, Met Office
#
# This file is part of iris-grib.
#
# iris-grib is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iris-grib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with iris-grib.  If not, see <http://www.gnu.org/licenses/>.
"""Unit tests for the :mod:`iris_grib` package."""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

from iris_grib.message import GribMessage
from iris_grib.tests import mock


def _make_test_message(sections):
    raw_message = mock.Mock(sections=sections)
    recreate_raw = mock.Mock(return_value=raw_message)
    return GribMessage(raw_message, recreate_raw)
