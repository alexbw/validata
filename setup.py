from setuptools import setup, find_packages

setup(
    name='validata',
    version='0.0.1',
    author='Alex Wiltschko',
    description='Continuous Integration for data',
    license='MIT',
    packages=find_packages(exclude='docs'),
    platforms='any',
    install_requires=['numpy'],
    include_package_data=True,
)
