# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'pylama==7.7.1',
    'pytest==6.2.4',
]
unit_test_requirements = [
    'pytest==6.2.4',
    'pytest-cov==2.12.1 '
]
integration_test_requirements = [
    'pytest==6.2.4 ',
    'pytest-cov==2.12.1'
]
run_requirements = [

]

with io.open('./word_hunt_builder/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="word-hunt-builder",
    version=version,
    author="Rodrigo Guimarães Araújo",
    author_email="rodrigoara27@gmail.com.br",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://gitlab.com/ratopythonista/word-hunt-builder",
    license="COPYRIGHT",
    description="Word Hunt Builder",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9'
    ],
)