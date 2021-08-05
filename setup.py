import os

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(BASE_DIR, "README.md")

with open(README) as file:
    long_description = file.read()

setup(
    name="pytest-pikachu",
    version="1.0.0",
    description="Show surprise when tests are passing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Charlie Hornsby",
    author_email="charlie.hornsby@hotmail.co.uk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    url="https://github.com/chornsby/pytest-pikachu",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"pytest11": ["pikachu = pytest_pikachu.plugin"]},
    install_requires=["pytest"],
)
