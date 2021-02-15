from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='aiofirestore',
    version='0.0.1',
    description='async version of google-cloud-firestore',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['aiofirebase'],
    author='henos',
    author_email='henos1029@gmail.com',
    keywords=['firebase', 'henos', 'aiofirestore', 'google-cloud-firestore'],
    url='https://github.com/henos1029/hoster'
)