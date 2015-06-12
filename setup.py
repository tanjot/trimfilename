from setuptools import setup

add_keywords = dict(
    entry_points={
        'console_scripts': ['trimfilename = trimfilename.main:main'],
    }, )

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(
    name="trimfilename",
    version="0.7.3",
    packages=['trimfilename'],
    license='GPLv3',
    description="Trim useless characters from filenames",
    long_description=long_description,
    url="https://github.com/tanjot/trimfilename",
    author="Tanjot Kaur",
    author_email="tanjot28@gmail.com",
    install_requires=requires,
    **add_keywords
)
