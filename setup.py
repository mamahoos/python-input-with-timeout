from setuptools import setup, find_packages
from input_with_timeout import (__title__, __version__, __url__,__license__, __author__,
                                __classifiers__, __author_email__, __description__)


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name=__title__.replace('_', '-')                                            ,
    version=__version__                                                         ,
    packages=find_packages(exclude=(r"python-input-with-timout\old_version", )) ,
    url=__url__                                                                 ,
    license=__license__                                                         ,
    author=__author__                                                           ,
    author_email=__author_email__                                               ,
    description=__description__                                                 ,
    long_description=long_description                                           ,
    long_description_content_type='text/markdown'                               ,
    keywords=['python', 'cross-platform', 'stdout', 'stin', 'console']          ,
    classifiers=__classifiers__                                                 ,
)
