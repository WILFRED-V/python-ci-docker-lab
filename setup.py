<<<<<<< HEAD
from setuptools import setup, find_packages

setup(
    name="python-ci-docker-lab",
    version="0.1",
    packages=find_packages(),
    py_modules=["app"],  # ensures app.py can be imported as a module
    install_requires=[
        # leave empty because GitHub Actions already installs from requirements.txt
    ],
)
=======
from setuptools import setup, find_packages

setup(
    name="python-ci-docker-lab",
    version="0.1",
    packages=find_packages(),
    py_modules=["app"],  # ensures app.py can be imported as a module
    install_requires=[
        # leave empty because GitHub Actions already installs from requirements.txt
    ],
)
>>>>>>> 87a9a599874d076713bcd28700083c90b52a725b
