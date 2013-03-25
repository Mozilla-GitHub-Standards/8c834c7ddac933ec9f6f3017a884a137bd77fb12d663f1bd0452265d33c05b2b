import os
from setuptools import setup, find_packages

__version__ = '0.1'

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'requests==1.1.0',
    'pyelasticsearch==0.3',
]

test_requires = requires + [
    'coverage',
    'monolith.web',
    'nose',
    'pyelastictest',
    'WebTest',
]

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()


setup(name='monolith.client',
    version=__version__,
    description='Mozilla Monolith Client',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web services",
    author='Mozilla Services',
    author_email='services-dev@mozilla.org',
    url='https://github.com/mozilla/monolith-client',
    license="Apache 2.0",
    packages=find_packages(),
    namespace_packages=['monolith'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=test_requires,
    test_suite="monolith.client",
    extras_require={'test': test_requires},
)
