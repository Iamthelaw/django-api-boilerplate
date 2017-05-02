# !/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    name='robohead-demo',
    packages=find_packages(exclude=['tests*', 'docs']),
    version='0.1.0',
    description='Demo admin application for robohead project',
    author='Anton Alekseev',
    license='MIT',
    author_email='robotehnik@me.com',
    url='https://github.com/robohead/demo',
    keywords=['django', 'djangorestframework'],
    install_requires=['Django', 'djangorestframework'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
