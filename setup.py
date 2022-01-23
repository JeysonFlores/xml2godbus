#!/usr/bin/python3
from distutils.core import setup

install_data = [
    ("bin/xml2godbus", ["src/main.py"]),
    ("bin/xml2godbus", ["src/interface.py"]),
    ("bin/xml2godbus", ["src/template.py"]),
    ("bin/xml2godbus", ["src/__init__.py"]),
]

setup(
    name="xml2godbus",
    version="1.0.0",
    author="Jeyson Flores",
    description="XML to godbus parser",
    url="https://github.com/JeysonFlores/xml2godbus",
    license="GNU GPL3",
    scripts=["xml2-godbus"],
    packages=["src"],
    data_files=install_data,
)
