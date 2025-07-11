import os

from setuptools import find_packages, setup

setup(
    name="sentinelpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Gustavo Viana",
    description="Modular cyber defense suite in Python",
    long_description=(
        open("README.md", encoding="utf-8").read()
        if os.path.exists("README.md")
        else ""
    ),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
