import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()
	
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='reusable-recipes-app',
	version='1.0.0',
	packages=['recipes_blog'],
	include_package_data=True,
	description='A django app for to create recipe blogs',
	long_description=README,
	url='https://github.com/hcurtis1',
	author='Henry Curtis',
	author_email='hcuk106@gmail.com',
	classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'Pillow',
        'django_forms_bootstrap',
        'django-disqus',
    ],
)