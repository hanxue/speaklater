import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_docs():
    result = []
    in_docs = False
    f = open(os.path.join(os.path.dirname(__file__), 'speaklater.py'))
    try:
        for line in f:
            if in_docs:
                if line.lstrip().startswith(':copyright:'):
                    break
                result.append(line[4:].rstrip())
            elif line.strip() == 'r"""':
                in_docs = True
    finally:
        f.close()
    return '\n'.join(result)

setup(
    name='speaklater3',
    author='Armin Ronacher, Thomas Waldmann',
    author_email='armin.ronacher@active-4.com, tw@waldmann-edv.de',
    version='1.4',
    url='https://github.com/ThomasWaldmann/speaklater',
    py_modules=['speaklater'],
    description='Implements a lazy string for python useful for use with gettext. This version is compatible with Python 3',
    long_description=get_docs(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Internationalization',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
