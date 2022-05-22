#!/usr/bin/env python

from distutils.core import setup

setup(
    name="builder",
    version="1.0",
    description="Build and push docker image",
    author="Tom Petr",
    author_email="trpetr@gmail.com",
    packages=["builder"],
    install_requires=["click"],
    entry_points={"console_scripts": ["builder=builder:main"]},
)
