# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='json-match',
      version='0.1',
      description='Verify if object json contains value expected.',
      long_description=open(README).read(),
      author="Flavio Henrique", author_email="flaviohenriqu@gmail.com",
      license="MIT",
      py_modules=['jmatch'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/flaviohenriqu/json-match/',)