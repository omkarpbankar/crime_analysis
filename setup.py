from setuptools import setup, find_packages

with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='src',
    verson='0.0.1',
    description="Package for dvc and data analytics",
    Long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/omkarpbankar/Crime_Analysis',
    author = "omkarpbankar",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    License="GNU",
    python_version="<=3.7",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas'
    ]

    )