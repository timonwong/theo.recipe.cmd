# -*- coding: utf-8 -*-
# Copyright (C)2007 'Ingencpeb'

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
This module contains the tool of theo.recipe.cmd
"""
from setuptools import find_packages, setup

name = 'theo.recipe.cmd'
version = '0.6.2'

setup(
    name=name,
    version=version,
    description="ZC Buildout recipe to execute commands in it's own shell",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGELOG.rst").read()),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Buildout",
    ],
    keywords='buildout, zc.buildout, recipe',
    author='Timon Wong',
    author_email='timon86.wang@gmail.com',
    url='https://github.com/timonwong/theo.recipe.cmd',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['theo.recipe', 'theo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    entry_points={
        "zc.buildout": [
            "default = %s:Cmd" % name,
            "sh = %s:Cmd" % name,
            "py = %s:Python" % name,
        ]
    }
)
