#! /usr/local/bin/python3.7

from setuptools import setup

setup(name='GCode',
      version='0.0.5',
      packages=['gcode',
                'gcode/primitive',
                'gcode/generators',
                'gcode/generators/Cpp',
                'gcode/generators/Xml',
                'gcode/ui',
                'gcode/modules',
                'gcode/modules/nodelet',
                'gcode/modules/nodelet/Cpp',
                'gcode/resources',
                'gcode/blueprints',
                'gcode/unit'],
      author='Marco Treglia',
      include_package_data=True,
      install_requires=[],
      license='MIT',
      )
