from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    readme = file.read()
 
setup(
    name='library_name',
    version='0.0.0',
    license='MIT License',
    author='Lincoln Oliver',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='lincolnolive@gmail.com',
    keywords='python library maker template',
    description='A template to make library make easier for python',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['twine'],
    url='https://github.com/lincolnolivr/pylib_template.git'
)