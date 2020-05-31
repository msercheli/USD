# REZ package for USD build

name = "usd"
version = "20.05"
description = "Pixar USD"
authors = ["Pixar"]

requires = [
    "python-3",
]

build_system = "cmake"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python")
