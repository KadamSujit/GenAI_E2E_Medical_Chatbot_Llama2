# This setup.py file is used to create local packages.
# (for e.g creating src as package so that files from this package will be able to be imported elsewhere).

# for this we use inbuilt setuptools lib
from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'Sujit Kadam',
    author_email= 'sujitpkadam1991@gmail.com',
    packages= find_packages(),
    install_requires = []

)
# find_packages() function looks for __init__.py consturctor and wherever it finds this __init__.py file, it considers it as a local package
