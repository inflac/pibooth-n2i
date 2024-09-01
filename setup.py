#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup

HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import pibooth_n2i as plugin  # nopep8 : import shall be done after adding setup to paths


def main():
    setup(
        name=plugin.__name__,
        version=plugin.__version__,
        description=plugin.__doc__,
        long_description=open(osp.join(HERE, 'README.md'), encoding='utf-8').read(),
        long_description_content_type='text/x-rst',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Natural Language :: English',
            'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        ],
        author="Inflac",
        url="https://github.com/inflac/pibooth-n2i",
        download_url="https://github.com/inflac/pibooth-n2i/archive/{}.tar.gz".format(plugin.__version__),
        license='GPLv3',
        platforms=['unix', 'linux'],
        keywords=[
            'Raspberry Pi',
            'camera',
            'photobooth',
            'N2i',
            'CMS'
        ],
        py_modules=['pibooth_n2i'],
        python_requires=">=3.8",
        install_requires=[
            'pibooth>=2.0.0'
        ],
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={'pibooth': ["pibooth_n2i = pibooth_n2i"]},
    )


if __name__ == '__main__':
    main()