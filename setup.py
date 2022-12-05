from setuptools import setup, find_packages
import codecs
import os
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'python library for easy creation of a telegram bot.'
LONG_DESCRIPTION = 'A package that allows you to create bots for telegram using its entire API.'

setup(
    name="tg_bottin",
    version=VERSION,
    author="Sweetie (Roma Fomkin)",
    author_email="<2004sweetheart2004@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyrogram', 'requests', 'aiohttp','datetime'],
    keywords=['python', 'bot', 'tg', 'tg bot', 'telegram', 'telegram bot', 'botting'],
    classifiers=[
        "Development Status :: 1 - will be finalized",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)