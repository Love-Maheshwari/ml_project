from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ." # this is the string that we want to remove from the requirements.txt file

def get_requirements(file_path:str)->List[str]:
    '''
    this function reads the requirements file and
    returns the list of requirements
    '''
    requirements = []
    with open('requirements.txt','r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # as reading the lines |n will be there so to handle that used replace.
 
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name = "Project_2",
    version = "0.0.1",
    author = "Love maheshwari",
    package = find_packages(),
    install_requires = get_requirements("requirements.txt")
)