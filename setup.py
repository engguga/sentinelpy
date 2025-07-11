from setuptools import find_packages, setup

setup(
    name="sentinelpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sentinel=sentinel:main",
        ],
    },
    python_requires=">=3.8",
)
