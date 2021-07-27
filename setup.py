#!/usr/bin/env python3
from setuptools import setup, find_packages

from umap import current_version

setup(
    name='umap',
    version=current_version,
    description='',
    author='NCC Group',
    license='GNU Affero General Public License v3.0',
    url='https://github.com/nccgroup/umap',
    packages=find_packages(),
    install_requires=[
        'pyserial'
    ],
    python_requires='>=3.0',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'umap=umap.umap:main',
        ],
    }
)

