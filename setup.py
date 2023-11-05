from setuptools import setup, find_packages

setup(
    name='sort-tracking',
    version='0.1.1',
    description='The modified version of sort tracking (https://github.com/abewley/sort) compatible with the Yolo Series',
    author='amish0',
    author_email='amishkumar562@gmail.com',
    url='https://github.com/amish0/Sort_tracking',
    # packages=find_packages(),
    install_requires=[
        'numpy',
        'PyYAML',
        'filterpy',
        'scikit-image',
        'lapx',
    ],
    packages=['tracking'],
)
