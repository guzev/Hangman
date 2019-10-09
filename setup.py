#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="game",
    version="0.0.0",
    author="Ivan Guzev",
    author_email="guzev1997@gmail.com",
    url="https://github.com/guzev/Hangman",
    license="MIT",
    packages=[
        "src",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pycodestyle",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pycodestyle",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
