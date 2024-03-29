from setuptools import setup, find_packages
from input_with_timeout import (__title__, __version__, __url__,__license__, 
                                __author__, __author_email__, __description__)

setup(
    name=__title__.replace('_', '-'),
    version=__version__,
    packages=find_packages(),
    url=__url__,
    license=__license__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=open('README.md', mode='rt').read(),
    keywords=['python', 'cross-platform', 'stdout', 'stin', 'console']
)
