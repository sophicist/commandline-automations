from setuptools import setup, find_packages

setup(
    name="jformat",
    version="0.0.1",  # Versioning: "0.0.1" is more standard for early versions
    description="Reformats files and outputs to stdout",
    long_description="A CLI tool for reformatting files and printing them to stdout.",
    long_description_content_type="text/markdown",  # Assuming you'll add a README file later
    install_requires=['click', 'colorama'],
    entry_points={
        'console_scripts': [
            'jformat = jformat.main:main',
        ],
    },
    author="John Kamau",
    author_email="kkamaujohn@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Assuming you'll use an MIT license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum version of Python required
)
