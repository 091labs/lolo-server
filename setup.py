from distutils.core import setup

setup (
    name = "lolo",
    packages = ['lolo',],
    package_dir={'lolo': 'src/lolo/usr/local/bin'},
    version = "0.3",
    url = "http://091labs.com",
    author = "Padraic Harley",
    author_email = "padraic@091labs.com",
    description = "library to manage 091 Labs status button",
    long_description = open('README.txt').read(),
    license = "Do What The Fuck You Want To Public License (WTFPL)",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: POSIX",
        "Programming Language :: C",
        "Programming Language :: Python"]
    )
