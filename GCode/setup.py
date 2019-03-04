#! /usr/local/bin/python3.7

from setuptools import setup

setup(name='GCode',
      version='0.0.4',
      packages=['gcode',
                'gcode/primitive',
                'gcode/generators',
                'gcode/generators/lib',
                'gcode/agent'],
      author='Marco Treglia',
      include_package_data=True,
      install_requires=[],
      license='MIT',
      )
