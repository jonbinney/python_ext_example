from distutils.core import setup, Extension

setup (name = 'PackageName',
       version = '1.0.0',
       description = 'This is a demo package',
       ext_modules = [Extension('demo', sources=['src/demo.c'])]
       )
