# -*- coding: utf-8 -*-

name = "usd"

version = "19.05"

description = \
    """
    Universal Scene Description
    """

authors = ["Pixar"]

requires = [
    "boost",
    "tbb",
    "OpenSubdiv",
    "glew",
    "openexr",
    "python",
    "ptex",
    "pyside",
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages")
    env.USD_ROOT = '{root}'

uuid = "repository.usdS"
