import ast
import re

from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name = 'docker_rest_service',
    version = version,
    url = 'https://github.com/alsbi/docker_rest_service',
    license = 'MIT',
    author = 'alsbi',
    author_email = 'feano4ik@gmail.com',
    description = 'Docker control service',
    long_description = open('README.md').read(),
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'flask',
        'requests_unixsocket',
    ],
    entry_points = {
        'console_scripts': [
            'docker_rest_service=docker_rest_service:main'
        ],
    }
)
