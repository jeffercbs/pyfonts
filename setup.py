import setuptools
from pyfonts import __version__

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="pyfonts",
    version=__version__,
    author="Jeferson Barrero",
    author_email="jebarrero14@gmail.com",
    description="",
    long_description=README,
    long_description_content_text="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    keywords="",
    entry_points={
        "console_scripts": ["pyfonts.main:main"]
    },
    classifiers=[]
)