#!/usr/bin/env python

import os
from setuptools import setup, find_packages

install_requires = [line.rstrip() for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))]

setup(
    name='eight',
    version='1.0.1',
    url='https://github.com/kislyuk/eight',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='Python 2 to the power of 3. A lightweight porting helper library.',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
