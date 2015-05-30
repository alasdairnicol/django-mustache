#!/usr/bin/env python

from distutils.core import setup

setup(name='django-mustache',
      version='0.1',
      author='Alasdair Nicol',
      author_email='alasdair@thenicols.net',
      packages=['django_mustache',
                'django_mustache.backend',
                'django_mustache.backend.mustache',
      ],
      requires=['pystache', 'django (>=1.8)'],
)
