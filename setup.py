import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-filer",
    version = "0.0.5a8",
    url = 'http://github.com/stefanfoulis/django-filer-cmsplugins',
    license = 'BSD',
    description = "django-cms plugins for django-filer",
    long_description = read('README'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = ['setuptools','django','django-cms',],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe = False
)