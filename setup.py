from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

# Import List from typing
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = [] 
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:  # Fixed 'Requirements' to 'requirements'
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject', 
    version='0.0.1',
    author='Deepesh', 
    author_email='d4deepesh@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)
