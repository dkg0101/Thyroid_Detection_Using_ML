from setuptools import setup,find_packages
from  typing import List

PROJECT_NAME = 'thyroid_detection'
VERSION = '0.0.1'
AUTHOR = 'Dhananjay Gurav'
DESCRIPTION ='This is end to end project for thyroid disease detection'
PACKAGES = ['thyroid']
REQUIREMENT_FILE_NAME = 'requirements.txt'


def get_requirements_list():
    """
    Description: This function is going to return  list of requirements
    mentioned inside requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .\n')
    


setup(
    name=PROJECT_NAME,
    version= VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires =get_requirements_list()
)

if __name__=="__main__":
    requirement = get_requirements_list()