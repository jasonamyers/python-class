# setup.py
from distutils.core import setup, Extension

setup(name="sample", 
      py_modules = ['sample.py'],
      ext_modules=[
          Extension("_sample",
                    ["sample_wrap.c"],
                    include_dirs = [],
                    library_dirs = ["."],
                    libraries = ['sample']
                  )
      ])
