from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    author="Maharshi Sen",
    author_email="maharshi.sen@fau.de",
    packages=find_packages(),
    install_requires=["random","unittest"],
)
