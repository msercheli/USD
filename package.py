# -*- coding: utf-8 -*-

name = "usd"

version = "19.03"

description = \
    """
    Universal Scene Description
    """

authors = ["Pixar"]

requires = [
    "boost",
    "tbb",
    "glew",
    "python",
    "ptex",
    "openexr",
    "OpenSubdiv",
    "pyside",
]

build_command = "pip install /home/marcelo/Dev/payload/numpy/numpy-1.16.2-cp27-cp27mu-manylinux1_x86_64.whl --prefix=/home/marcelo/packages/numpy/1.16.2"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages")
    env.NUMPY_ROOT = '{root}'

uuid = "repository.numpy"
