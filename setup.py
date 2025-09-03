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
