#!/bin/sh

# Need to manually dnf install:

# sudo dnf install ...
# zlib-devel
# libX11-devel
# mesa-libGL-devel
# mesa-libGLU-devel
# glew
# glew-devel

# This is where `uic` for qt5 is (to replace pyside2-uic executable)
export PATH="/usr/lib64/qt5/bin":$PATH

python build_scripts/build_usd.py \
    /home/marcelo/dev/build/usd/20.11/debug \
    --debug \
    --build-shared \
    --python \
    --usd-imaging \
    --ptex \
    --openvdb \
    --openimageio \
    --no-usdview \
    --no-opencolorio \
    --no-materialx \
    --no-alembic \
    --no-hdf5 \
    --no-draco \
    --no-tests \
    --no-examples \
    --no-tutorials \
    --no-docs

# The following in your PYTHONPATH environment variable:
#    /home/marcelo/dev/build/usd/20.05/lib/python

#    The following in your PATH environment variable:
#    /home/marcelo/dev/build/usd/20.05/bin
