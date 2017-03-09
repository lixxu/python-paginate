"""
python-paginate
--------------

Pagination support for python web frameworks (study from will_paginate).
Supported CSS: bootstrap2&3&4, foundation, ink, uikit and semanticui
Supported web frameworks: Flask, Tornado, Sanic
"""
from setuptools import setup

setup(
    name='python-paginate',
    version='0.3.4',
    url='https://github.com/lixxu/python-paginate',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple paginate support for python web frameworks',
    long_description=__doc__,
    packages=['python_paginate', 'python_paginate.css', 'python_paginate.web'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3.3',
    ]
)
