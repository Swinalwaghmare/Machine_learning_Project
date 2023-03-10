from setuptools import setup, find_packages
from typing import List

# Declaring varibales for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Swinal"
DESCRIPTION = "This is my first project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """This function is going to return
    list of requirements mention in requrements.txt file 

    Returns:
        List[str]: This function is going to return a list which 
        contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), # Where ever it is seeing __init__ it brings us as a package
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())