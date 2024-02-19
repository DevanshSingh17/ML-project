# by using setup.py we can use our machine learning project as an package where later we can use it anywhere else

from setuptools import find_packages,setup
from typing import List

hypen="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of function requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen)
            
        
setup(
    name ="ML project",
    version ="0.0.1",
    author="DEVANSH",
    author_email="devansh.shivdas.tomar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    )
