import codecs
from setuptools import setup

TWPY_VERSION = '1.1'
TWPY_DOWNLOAD = ('https://github.com/0x0ptim0us/twpy/tarball/' + TWPY_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()


setup(
	name='twpy',
	packages=['twpy', 'twpy.config', 'twpy.core', 'twpy.exceptions', 'twpy.models', 'twpy.serializers', 'twpy.utils'],
	version=TWPY_VERSION,
	description='Twpy is an open-source intelligence library for twitter, NO API - NO LIMIT ',
	long_description=read_file('README.rst'),
	license='MIT',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/0x0ptim0us/twpy',
	download_url=TWPY_DOWNLOAD,
	keywords=['python3', 'twitter', 'twitter api', 'twpy', 'no api'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Natural Language :: English',
	],
	install_requires=[
		'requests',
		'beautifulsoup4',
		'pandas'
	],

)
