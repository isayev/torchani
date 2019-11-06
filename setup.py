from setuptools import setup, find_packages
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_attrs = {
    'name': 'torchani',
    'description': 'PyTorch implementation of ANI',
    'long_description': long_description,
    'long_description_content_type': "text/markdown",
    'url': 'https://github.com/aiqm/torchani',
    'author': 'Xiang Gao',
    'author_email': 'qasdfgtyuiop@gmail.com',
    'license': 'MIT',
    'packages': find_packages(),
    'include_package_data': True,
    'use_scm_version': True,
    'setup_requires': ['setuptools_scm'],
    'install_requires': [
        'torch',
        'lark-parser',
    ],
}

if sys.version_info[0] < 3:
    setup_attrs['install_requires'].append('typing')

setup(**setup_attrs)
