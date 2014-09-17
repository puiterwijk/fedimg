# This file is part of fedimg.
# Copyright (C) 2014 Red Hat, Inc.
#
# fedimg is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# fedimg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with fedimg; if not, see http://www.gnu.org/licenses,
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  David Gay <dgay@redhat.com>
#

from setuptools import setup, find_packages

setup(
    name='fedimg',
    version='0.2.6',
    description='A service that listens to the Fedmsg bus and'
                ' automatically uploads built Fedora cloud images'
                ' to internal and external cloud providers.',
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Affero General Public License"
        " v3 or later (AGPLv3+)",
    ],
    keywords='python Fedora cloud image uploader service',
    author='David Gay',
    author_email='oddshocks@riseup.net',
    url='https://github.com/fedora-infra/fedimg',
    license='AGPLv3+',
    include_package_data=True,
    zip_safe=False,
    install_requires=["fedmsg",
                      "apache-libcloud",
                      "paramiko"],
    tests_require=['nose'],
    packages=find_packages(),
    entry_points="""
    [moksha.consumer]
    kojiconsumer = fedimg.consumers:KojiConsumer
    """,
)
