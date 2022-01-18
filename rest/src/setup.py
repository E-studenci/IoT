from setuptools import setup, find_packages
from distutils.core import setup

setup(
    name='api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'attrs==21.4.0',
        'certifi==2021.10.8',
        'click==8.0.3',
        'colorama==0.4.4',
        'Deprecated==1.2.13',
        'Flask==2.0.2',
        'Flask-HTTPAuth==4.5.0',
        'Flask-Login==0.5.0',
        'itsdangerous==2.0.1',
        'Jinja2==3.0.3',
        'jsonschema==4.4.0',
        'MarkupSafe==2.0.1',
        'pymongo==4.0.1',
        'pyrsistent==0.18.1',
        'python-dotenv==0.19.2',
        'redis==4.0.2',
        'Werkzeug==2.0.2',
        'wrapt==1.13.3',
    ],
    include_package_data=True
)
