from setuptools import setup, find_packages
import os


INSTALL_REQUIREMENTS = [
]

setup(
    author='Michael Wayman',
    name='django-slowdown',
    version='0.1.0',
    description='slow down Django requests for better development',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/michaelwayman/django-slowdown',
    license='MIT',
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
)