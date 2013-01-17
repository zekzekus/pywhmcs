from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.0.2'

install_requires = [
    'requests',
    'simplejson',
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='pywhmcs',
    version=version,
    description="WHMCS Client Library",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='whmcs library http api',
    author='Zekeriya Koc',
    author_email='zekzekus@gmail.com',
    url='https://github.com/zekzekus/pywhmcs',
    license='Gnu General Public License v3',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pywhmcs=pywhmcs:main']
    }
)
