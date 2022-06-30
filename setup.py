from setuptools import setup
from bupytest import __version__

with open(f'README.md', 'r') as reader:
    full_doc = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='bupytest',
    description='Perform fast and detailed unit tests with BuPyTest.',
    long_description_content_type='text/markdown',
    long_description=full_doc,
    version=__version__,
    license='GPL-3.0',
    packages=['bupytest'],
    project_urls={
        'Source code': 'https://github.com/jaedsonpys/bupytest',
        'License': 'https://github.com/jaedsonpys/bupytest/blob/master/LICENSE',
        'Documentation': 'https://github.com/jaedsonpys/bupytest/blob/master/README.md'
    }
)
