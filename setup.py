import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prioQbyrobi", # Replace with your own username
    version="2.0.2",
    author="Md Robiuddin",
    author_email="mrrobi040@gmail.com",
    description="A package for priority queue to make A* Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mrrobi/prioQ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
