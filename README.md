# pylib_template
A quick template to create new python libraries 


# Publish Process

1 - Run the command 'python setup.py sdist'
2 - In case you don't have it yet: 'pip install twine'
3 - To create a test repository use run 'twine upload --repository-url https://test.pypi.org/legacy/ dist/*'
4 - To create the real repository run 'twine upload dist/*'
