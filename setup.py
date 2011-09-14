from distutils.core import setup
from realtimecongress import __version__

long_description = open('README.md').read()

setup(name="python-realtimecongress",
      version=__version__,
      py_modules=["realtimecongress"],
      description="A library for interacting with the Real Time Congress API",
      author="Dan Drinkard <dan.drinkard@gmail.com>",
      author_email = "dan.drinkard@gmail.com",
      license="BSD",
      url="http://github.com/sunlightlabs/python-realtimecongress",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8", "requests"]
      )
