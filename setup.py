"""
python-paginate
-----------------

Pagination support for python web frameworks (study from will_paginate).
Supported CSS: bootstrap2&3&4, foundation, ink, uikit and semanticui, metro4
Supported web frameworks: Flask, Tornado, Sanic
"""
import io
import os.path

from setuptools import setup

work_dir = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(work_dir, "python_paginate/__init__.py")

version = ""
with io.open(fp, encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__ = "):
            version = line.split("=")[-1].strip().replace("'", "")
            break

setup(
    name="python-paginate",
    version=version.replace('"', ""),
    url="https://github.com/lixxu/python-paginate",
    license="BSD-3-Clause",
    author="Lix Xu",
    author_email="xuzenglin@gmail.com",
    description="Simple paginate support for python web frameworks",
    long_description=__doc__,
    packages=["python_paginate", "python_paginate.css", "python_paginate.web"],
    zip_safe=False,
    platforms="any",
    install_requires=["six"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 3",
    ],
)
