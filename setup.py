from setuptools import setup
import json


def readme():
  with open("README.md") as readme:
    return readme.read()


def package_info():
  with open("package_info.json") as package:
    return json.load(package)


def requirements():
  with open('requirements.txt') as reqs:
    return list(filter(lambda line: line, map(str.strip, reqs)))


setup(
  long_description=readme(),
  install_requires=requirements(),
  scripts=["bin/dsi"],
  **package_info()
)