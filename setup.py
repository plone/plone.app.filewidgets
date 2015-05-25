from setuptools import setup, find_packages

version = '1.0.0.dev0'

long_description = \
    open("README.rst").read() + "\n" + open("CHANGES.rst").read()

setup(name='plone.app.filewidgets',
      version=version,
      description="more robust file input widgets for plone",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords='plone widgets',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://github.com/plone/plone.app.filewidgets',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Acquisition',
          'DateTime'
      ],
      extras_require=dict(
          test=[
              'plone.app.contenttypes',
              'plone.app.testing'
          ]
      ),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
