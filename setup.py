from setuptools import setup

setup(
	
	name='hamming-app',
	packages=['flask-app', 'hammingclasses'],
	include_package_data=True,
	install_requires=[
		'flask',
		'numpy'
	],
)