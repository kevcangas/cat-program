#IMPORTANT:
#To install the package is necessary pre-install setuptools in your environment
#When you did the last, type: "pip install -e <directory-of-your-package>" in the terminal to finish the installation 
#It's necessary have the requirements.txt archive before the installation

from setuptools import setup
import os

#requirements.txt lecture
REQUIREMENTS_PATH = os.path.join(os.path.curdir,'requirements.txt')
with open(REQUIREMENTS_PATH, 'r') as f:
    requires = f.readlines()
    for i in range(len(requires)):
        requires[i] = requires[i].replace('\n','')

#setup
setup(
   name='programa_rasp',
   version='0.0.1',
   description='Este programa contiene todo el control del gato perteneciente a la raspberry',
   author='KevCangas',
   author_email='kev162020@gmail.com',
   packages= [os.path.abspath(os.getcwd())],  # would be the same as name
   install_requires=requires #external packages acting as dependencies
)