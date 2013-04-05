#from distutils.core import setup
from setuptools import setup, find_packages

# http://guide.python-distribute.org/quickstart.html
# python setup.py sdist
# python setup.py register
# python setup.py sdist upload
# pip install cyclone-rest-handler
# pip install cyclone-rest-handler --upgrade --no-deps
# Manual upload to PypI
# http://pypi.python.org/pypi/cyclone-rest-handler
# Go to 'edit' link
# Update version and save
# Go to 'files' link and upload the file


tests_require = [
]

install_requires = [
]

setup(name='cyclone-rest-handler',
      url='https://github.com/gleicon/cyclone-rest-handler',
      author="gleicon",
      author_email='gleicon@gmail.com',
      keywords='python cyclone rest handler',
      description='A simple Python Cyclone handler that manage Rest requests automatically.',
      license='MIT',
      classifiers=[
          # 'Framework :: Tornado',
          'Operating System :: OS Independent',
          'Topic :: Software Development'
      ],

      version='0.0.1',
      install_requires=install_requires,
      tests_require=tests_require,
      # test_suite='runtests.runtests',
      # extras_require={'test': tests_require},

      packages=find_packages(),
)

