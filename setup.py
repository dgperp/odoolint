from setuptools import setup, find_packages

setup(
    name="odoolint",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flake8",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "odoolint=odoolint.main:main",
        ],
    },
)
