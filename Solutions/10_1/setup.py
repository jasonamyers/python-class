# setup.py
#
# For testing, run this script using 'python setup.py build_ext --inplace'

from distutils.core import setup, Extension

setup(name="sample", 
      ext_modules=[Extension("sample",
                   ["sample.c","pysample.c"])]
      )

