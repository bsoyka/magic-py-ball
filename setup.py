from setuptools import setup, find_packages

with open("README.md") as file:
    long_description = file.read()

setup(
    name="magic_py_ball",
    version="2.2.0",
    author="Ben Soyka",
    author_email="bensoyka@icloud.com",
    description="A simple magic 8 ball",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsoyka/magic-py-ball",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=2.7",
    project_urls={
        "Source": "https://github.com/bsoyka/magic-py-ball",
        "Changelog": "https://github.com/bsoyka/magic-py-ball/releases",
    },
)
