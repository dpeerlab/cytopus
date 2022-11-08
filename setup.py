from setuptools import setup, find_packages

setup(
    name='cytopus',
    version='1.2',
    packages=["cytopus"],
    install_requires = [
        "pandas>1.3",
        "numpy>1.2",
        "networkx>2.7",
        "matplotlib-base>3.4"]        
)
