#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='whatmp3',
      version='v3.8',
      # Modules to import from other scripts:
      packages=find_packages(),
      # Executables
      scripts=["whatmp3.py"],
     )
