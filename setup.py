from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

import numpy 

setup(name='clodius',
    ext_modules=cythonize([Extension("clodius.fast", ["clodius/fast.pyx"])]),
     include_dirs=[numpy.get_include()],
      version='0.2.2',
      description='Tile generation of big data',
      author='Peter Kerpedjiev',
      author_email='pkerpedjiev@gmail.com',
      url='',
      packages=['clodius'],
      install_requires=[
                    'cython',
                    'numpy' ],
      scripts=['scripts/make_single_threaded_tiles.py']
     )
