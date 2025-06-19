from setuptools import find_packages,setup
from typing import list 

def get_requirements(file_path:str)--> List[str]:
       '''
       THis functioin will return the list of requirements
       '''
       requirements=[]
       with open(file_path) as file_obj:
              requirements=file_obj.readlines()


setup(
name= 'mlproject',
version='0.0.1',
author='Krish'
author_email='krishnaik06@gmail.com',
packages=find_packages()
install_requires=get_requirements['pandas','numpy','seaborn']

)
