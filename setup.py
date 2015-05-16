from setuptools import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['trimfilename = trimfilename.main:main'],
        },
)

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(

    name="trimfilename",
    version="0.5",
    license='GPLv3',
    description="Remove string patterns from filenames",
    url="https://github.com/tanjot/trimfilename",
    author="Tanjot Kaur",
    author_email="tanjot28@gmail.com",
    packages=['trimfilename'],
    **add_keywords
)
