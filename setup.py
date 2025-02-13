'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    
    requirement_list:List[str] = []
    
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and ignore -e .
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except Exception as e:
        raise e
    
    return requirement_list

setup(
    name="network_security",
    version="0.0.1",
    author="Kevin",
    author_email="kevinkamzw@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)