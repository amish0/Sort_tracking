from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='Sort_Tracking',
    version='0.1.0',
    description='The modified version of sort tracking (https://github.com/abewley/sort) compatible with the Yolo Series',
    author='Annomious',
    author_email='amishkumar562@gmail.com',
    url='https://github.com/amish0/Sort_tracking',
    packages=find_packages(),
    install_requires=required_packages,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
