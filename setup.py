from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'VanityMnem',
    version = '0.0.1',
    author = 'Valerio Vaccaro',
    author_email = 'valerio.vaccaro@gmail.com',
    license = 'MIT',
    description = 'create your vanity mnemonics',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/valerio-vaccaro/vanitymnem',
    py_modules = ['vanitymnem'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        vanitymnem=vanitymnem:main
    '''
)
