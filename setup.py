import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cltk_readers",
    version="0.0.1",
    description="Corpus reader extension for the Classical Language Toolkit ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/diyclassics/cltk_readers",
    author="Patrick J. Burns",
    author_email="patrick@diyclassics.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["cltk_readers"],
    include_package_data=True,
    install_requires=["cltk", "pyuca"],
)
