from setuptools import find_packages, setup
from typing import List
hypen='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    name="student performance",
    version="0.0.1",
    author="faizan",
    author_email="sidsiquifaizxxn459@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)