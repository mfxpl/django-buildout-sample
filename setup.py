from setuptools import setup, find_packages

setup(
    name = "django-shorturls",
    version = "1.0",
    url = 'https://github.com/mfxpl/django-buildout-sample.git',
    license = 'GNU',
    description = "A short URL handler for Django apps.",
    author = 'Michał Frąckowiak',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)