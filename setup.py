#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'putrusinu',
]

# with open('README.rst') as f:
#     readme = f.read()
# with open('HISTORY.rst') as f:
#     history = f.read()

setup(
    name='putrusinu',
    version='0.2.0',
    description='Putrusinu - A collection of tools to manage data and data streams.',
    # long_description=readme + '\n\n' + history,
    author='Antonio Lima',
    author_email='anto87@gmail.com',
    url='https://github.com/themiurgo/putrusinu',
    packages=packages,
    package_data={'': ['LICENSE',]},
    package_dir={'putrusinu': 'putrusinu'},
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ),
    install_requires=[
    ],
    entry_points={
      'console_scripts': [
        'streamsample = putrusinu.streamsample:main',
        'range = putrusinu.range:main',
        'colconv = putrusinu.colconv:main',
        'repeat = putrusinu.repeat:main',
        'counter = putrusinu.counter:main',
      ]
    }
)
