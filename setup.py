import os
from setuptools import setup, Command, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf build dist *.pyc *.tgz *.egg-info')


setup(name = 'pol_sim',
      version = '0.1',
      description = '''Code for Modeling Polarization in Optics''',
      long_description = readme(),
      author = 'Katie Harrington',
      author_email = 'katie.megan.harrington@gmail.com',
      license = 'MIT',
      packages = ['pol_sim'],
      package_dir = {'pol_sim':'pol-sim'},
      cmdclass={'clean':CleanCommand,},
      #scripts = []
      )
