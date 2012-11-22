# -*- coding: utf-8 -*-
"""
    PyCharm	
    ~~~~~~

    :copyright: (c) 2012 by ytjohn
    :license: BSD, see LICENSE for more details.
"""

from distutils.core import setup

setup(
    name='SecureStore',
    version='0.1.0',
    author='John Hogenmiller',
    author_email='john@hogenmiller.net',
    packages=['securestore'],
    url='https://github.com/ytjohn/securestore',
    license='LICENSE.txt',
    description='Secure token storage for passwords and other sensitive data.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pycrypto >= 2.4.1",
        ],
)
