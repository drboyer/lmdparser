from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["tests"]  # only run tests in tests/ directory
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)


setup(name='lmdparser',
      version='0.0.1',
      description='Module to parse data stored in Lake Meteorological Data format',
      url='https://github.com/drboyer/lmdparser',
      author='Devin Boyer',
      author_email='drb5272@gmail.com',
      license='MIT',
      packages=['lmdparser'],
      tests_require=['pytest'],
      cmdclass = {'test': PyTest},
      zip_safe=False)