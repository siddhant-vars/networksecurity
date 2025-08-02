from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found! ")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Siddhant Varshney",
    author_email="siddhantvarshney446@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)