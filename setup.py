from setuptools import find_packages, setup
from typing import List

HYPED_DOT_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPED_DOT_E in requirements:
            requirements.remove(HYPED_DOT_E)

        return requirements
    




setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Yash',
    author_email= 'agarwal.yash800@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)