# -*- coding: utf-8 -*-
from setuptools import setup
import python_q4m
from python_q4m import __version__, __license__, __author__, __doc__

if __name__ == '__main__':
    setup(
        name         = "python_q4m",
        version      = __version__,
        py_modules   = ["python_q4m"],
        packages     = ('python_q4m',),
        description  = 'Q4M operation wrapper',
        long_description = __doc__,
        author       = __author__,
        url          = 'http://github.com/cubicdaiya/python-q4m',
        author_email = 'cubicdaiya@gmail.com',
        keywords     = 'q4m, mysql, queue',
        license      = __license__,
        classifiers  = ["Development Status :: 5 - Production/Stable",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: GNU General Public License (GPL)",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"]
    )
