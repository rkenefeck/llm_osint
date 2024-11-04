from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="llm_osint",
    version="0.0.1",
    description="Fork of original by Shrivu Shankar",
    url="https://github.com/rkenefeck/llm_osint",
    author="Rob Kenefeck",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)
