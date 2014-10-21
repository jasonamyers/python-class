# setup.py
#
# Use this file to build a stand-alone shared library on your machine
# if you can't figure out how to do it manually

from distutils.core import setup, Extension

setup(name="libsample", 
      ext_modules=[Extension("libsample", ["sample.c"])]
      )

