from setuptools import setup, find_packages

exec(open('cktesting/version.py').read())

f = open('README.md', 'r')
__long_description__ = f.read()
f.close()

install_requires = []
with open('requirements.txt') as f:
    for line in f.read().splitlines():
        install_requires.append(line)

setup(
    name='cktesting',
    version=__version__,
    description='CKTesting: Use Content King to automate CI/CD testing',
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    author='JR Oakes',
    author_email='jroakes@gmail.com',
    url='https://github.com/jroakes/cktesting',
    license='Apache-2.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=[
        'jenkins',
        'testing',
        'seo',
        'travisci',
        'content king',
    ],
    packages=find_packages(exclude=['ez_setup', 'tests*']), # TODO: Fix this
    package_data={'cktesting': ['templates/*']}, # TODO: Fix this
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        cktesting = cktesting.main:main
    """,
)
