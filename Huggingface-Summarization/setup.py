from setuptools import setup, find_packages

# Reading requirements from requirements.txt
with open('requirements.txt', 'r') as f:
    requirements = [line for line in f.read().split('\n') if line]
print(requirements)
setup(
    name='sumarize',
    description="Demo Python CLI tool to summarize using Hugging Face",
    packages=find_packages(),
    author='John Kamau',
    entry_points={
        'console_scripts': [
            'sumarize = summary.main:main',
        ],
    },
    install_requires=requirements,  # Corrected key name
    version="0.0.1",
    url=""  # Add your project URL here if available
)
