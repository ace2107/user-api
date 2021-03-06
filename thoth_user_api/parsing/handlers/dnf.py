#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-user-api
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Parse packages installed using dnf."""

import attr

from .yum import HandlerBase


@attr.s
class DNF(HandlerBase):
    """Handle extracting packages from build logs - dnf installer."""

    def run(self, input_text: str) -> dict:
        """Find and parse installed package-versions from a build log."""
        return {}


# It looks like the output of dnf is same as for yum.
# Omit implementation and registering for now.
# HandlerBase.register(DNF)
