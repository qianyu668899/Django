import os
from setuptools import setup
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-polls',
	version='0.1',
	package=['polls'],
	include_package_data=True,
	license='BSD License',
	description='A simple Django app to conduct Web-based polls.',
	long_description=README,
	url='http://www.example.com/',
	author='Yu Qian',
	author_email='yqian33@uwo.ca',
	classifiers=[
		'Environment :: Web Environment',
		'Frameworm :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],

)