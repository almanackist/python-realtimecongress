from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-realtimecongress",
      version="0.1.0",
      py_modules=["realtimecongress"],
      description="A library for interacting with the Real Time Congress API",
      author="Dan Drinkard <dan.drinkard@gmail.com>",
      author_email = "dan.drinkard@gmail.com",
      license="BSD",
      url="http://github.com/dandrinkard/python-realtimecongress",
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
