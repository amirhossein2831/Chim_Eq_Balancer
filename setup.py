from setuptools import setup, find_packages

setup(
    name='chemical_eq_balancer',
    version='0.2',
    packages=find_packages(),
    install_requires=['numpy'],
    author='AmirHossein',
    author_email='amirmemool12@gmail.com',
    description='a package to balance simple chemical equations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amirhossein2831/Chim_Eq_Balancer',
    license='MIT',
)
