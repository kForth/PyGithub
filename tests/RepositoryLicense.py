############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Kestin Goforth <kgoforth1503@gmail.com>                       #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from . import Framework


class RepositoryLicense(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.license = self.g.get_user("PyGithub").get_repo("PyGithub").license

    def testAttributes(self):
        self.assertEqual(self.license.key, "lgpl-3.0")
        self.assertEqual(self.license.name, "GNU Lesser General Public License v3.0")
        self.assertEqual(self.license.node_id, "MDc6TGljZW5zZTEy")
        self.assertEqual(self.license.spdx_id, "LGPL-3.0")
        self.assertEqual(self.license.url, "https://api.github.com/licenses/lgpl-3.0")
