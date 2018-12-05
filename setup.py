from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='urssediscord',
    packages=find_packages(),  # this must be the same as the name above
    version='0.0.1',
    description='Discord bot for the UR SSE Discord.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake, Quinn Basr',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/ShawnClake/Discord-SSE-Bot',
    keywords=[],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'discord.py'
    ],
)
