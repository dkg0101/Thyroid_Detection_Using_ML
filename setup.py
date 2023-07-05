from setuptools import setup,find_packages
from  typing import List

PROJECT_NAME = 'thyroid_detection'
VERSION = '0.0.1'
AUTHOR = 'Dhananjay Gurav'
DESCRIPTION ='This is end to end project for thyroid disease detection'

REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPEN_E_DOT = '-e .'

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return  list of requirements
    mentioned inside requirements.txt file
    """
    requirements=[]
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = requirement_file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)


    return requirements
    


setup(
    name=PROJECT_NAME,
    version= VERSION,
    author=AUTHOR,
    author_email='dkgurav0101@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires =get_requirements_list()
)

if __name__=="__main__":
    requirement = get_requirements_list()