from setuptools import setup

setup(
    name='restkiss-haystack',
    version='0.1.0',
    packages=['restkiss_haystack'],
    install_requires=['Django', 'django-haystack', 'restkiss'],
    url='https://github.com/CraveFood/restkiss-haystack',
    license='MIT',
    author='Bruno Marques',
    author_email='bruno@bmarques.net',
    description='Integration of the Restkiss and Haystack libraries for Django',
    long_description=open('README.md', 'r').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
