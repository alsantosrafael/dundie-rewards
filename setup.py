from xml.etree.ElementPath import find
from setuptools import setup, find_packages

setup(
  name="dundie",
  version="0.1.0",
  description="Reward Point System for Dunder Mifflin Company",
  author="Rafael Almeida",
  packages=find_packages(),
)