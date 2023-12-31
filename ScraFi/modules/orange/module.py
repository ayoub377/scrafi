# -*- coding: utf-8 -*-

# Copyright(C) 2021      Zhor Abid
#
# This file is part of a woob module.
#
# This woob module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This woob module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this woob module. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals


from woob.tools.backend import Module, BackendConfig
from woob.tools.value import ValueBackendPassword
from woob.capabilities.bill import CapDocument

from .browser import OrangeBrowser


__all__ = ['OrangeModule']


class OrangeModule(Module, CapDocument):
    NAME = 'orange'
    DESCRIPTION = 'Orange'
    MAINTAINER = 'Zhor Abid'
    EMAIL = 'zhor.abid@gmail.com'
    LICENSE = 'LGPLv3+'
    VERSION = '3.1'

    BROWSER = OrangeBrowser

    CONFIG = BackendConfig(
        ValueBackendPassword('login', label='Utilisateur', masked=False),
        ValueBackendPassword('password', label='Mot de passe', masked=True)
    )

    def create_default_browser(self):
        return self.create_browser(self.config)

    def connect(self):
        return self.browser.connect()

    def get_bills(self, date):
        return self.browser.get_bills(date)