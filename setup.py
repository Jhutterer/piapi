"""
piapi module stands for (Cisco) Prime Infrastructure API.
The module implements the PIAPI class which helps interacting with the Cisco Prime Infrastructure REST API using
simple methods that can either request data or request an action.

The Cisco Prime Infrastructure API is a REST API which exposes several resources that can be of 2 types:
    * Data resources: expose some data collected by the software which can be retrieved (e.g: client summary).
    * Service resources: expose some service that can modify the configuration of the software (e.g: modify/update an Access Point)

The REST API is applying request rate limiting to avoid server's overloading. To bypass this limitation, especially
when requesting data resources, the PIAPI uses multithreading requests (grequests library) with an hold time between
chunk of requests. Please check the documentation to knowns more about rate limiting.

Also note that the piapi module only works with the JSON structure exposed by the REST API. The module doesn't support
the default XML structure.

Please check your Cisco Prime REST API available at https://{server-name}/webacs/api/v1/

test modification
"""
from setuptools import setup

setup(
    name='piapi',
    version='0.1.4',
    py_modules=['piapi'],
    install_requires=['requests>=2.4.0'],
    platforms='any',
    url='https://github.com/maximumG/piapi',
    download_url='https://github.com/maximumG/piapi/tarball/0.1.3',
    license='Apache',
    author='maximumG',
    author_email='mgerges@stubbynet.com',
    description='Cisco Prime Infrastructure REST API for python',
    long_description=__doc__,
    keywords=["Cisco", "Prime", "API", "REST", "request"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
