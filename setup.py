#!/usr/bin/env python


"""Setup script for Robot's MongoDB Library distributions"""

from setuptools import setup

import sys
import os

sys.path.insert(0, os.path.join('src', 'MongoDBLibrary'))

from version import VERSION


def main(scriptargs):
    setup(name='robotframework-mongodblibrary',
          version=VERSION,
          description='Mongo Database utility library for Robot Framework',
          author='Jerry Schneider',
          author_email='jerry@iplantcollaborative.org',
          url= 'https://github.com/',
          package_dir={'': 'src'},
          packages=['MongoDBLibrary'],
          install_requires=['robotframework', 'pymongo>=3.0.0'],
          script_args=scriptargs
          )
        

if __name__ == "__main__":
    main(sys.argv[1:])
