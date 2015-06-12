import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = '0.0.2'

setup(
    name='fifo',
    version=version,
    packages=['fifo'],
    install_requires=['redis >= 2.10.0'],
    include_package_data=True,
    license='BSD License',
    description='A simple redis based task queue for python',
    long_description=README,
    url='http://github.com/fergalwalsh/fifo',
    download_url='https://github.com/fergalwalsh/fifo/tarball/%s' % version,
    author='Fergal Walsh',
    author_email='fergalwalsh@gmail.com',
)
