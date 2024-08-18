from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="odoolint",
    version="1.0.6",
    description="A comprehensive linting tool for Odoo modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgperp/odoolint",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="odoo, linter, development, tools",
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=[
        "flake8",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "odoolint=odoolint.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/dgperp/odoolint/issues",
        "Source": "https://github.com/dgperp/odoolint/",
    },
)
