from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='FlaskRestful with mysql connector-Openshift template',

      # PEP 440 -- Version Identification and Dependency Specification
      version='0.0.1',

      # Project description
      description='FlaskRestful with mysql connector template app for OpenShift',
      long_description=readme,

      # Author details
      author='James Pavlic',
      author_email='james_pavlic@outlook.com',

      # Project details
      url='https://github.com/jpavlic/flask-openshift',
      license="GNU v3",

      # Project dependencies
      install_requires=requirements,
      )
