from codecs import open as codecs_open
from setuptools import setup, find_packages



setup(name='testpy',
      version='0.0.1',
      description=u"Skeleton of a Python package",
      long_description='long_description',
      classifiers=[],
      keywords='',
      author=u"Sean Gillies",
      author_email='sean@mapbox.com',
      url='https://github.com/pratikyadav/testpy',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      testpy=testpy.scripts.cli:cli
      """
      )
