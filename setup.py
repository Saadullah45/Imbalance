from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a requirements.txt file.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            line = line.replace("\n", "")
            if line!= '-e.':
                requirements.append(line)
    return requirements

setup(
    name="Imbalance",
    version="0.01",
    author="SaadUllah",
    author_email="saadullah45@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)