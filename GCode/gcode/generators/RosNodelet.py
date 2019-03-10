# Designed for python 3.7

# Copyright 2019 Marco Treglia
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; # OR #BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from gcode import Dictionary
from gcode.unit.Atoms import Atom, Logger, File, List
from gcode.primitive.filesystem import module_path, path, read, exists
import gcode

SUPPORTED_MODE = ['RosNodelet']


'''
    Component
'''

green = 6770
white = 6277

DATA = 'data'

MODULE_PATH = module_path(gcode)

relative_path = lambda file :  f'{MODULE_PATH}/resources/{file}'


'''
    Ros Nodelet Component
____________________
'''


'''
    Resources
'''
white = 6277


class ResourcesRosNodelet(Logger):
    headers = List('Headers', File('IComponentHeader', relative_path('IComponentv1.h')))

    def load_resource(self):
        self.Log('Reading resources', white)
        for file in self.headers():
            self[file.name] = file.read()


'''
    Variable
'''


class VariableRosNodelet(Dictionary):
    mode = None
    header = None
    cpp = None
    xml = None
    pkgxml = None
    cmake = None


'''
    Interface
'''


class InterfaceRosNodeletComponet(ResourcesRosNodelet, VariableRosNodelet):
    def __init__(self, content=None):
        super().__init__(content ['name'])
        self.data = content
        self.load_resource()


'''
    RosNodelet
'''


class RosNodelet(InterfaceRosNodeletComponet):

    def _header(self):
        pass

    def _cpp(self):
        pass

    def _xml(self):
        pass

    def _packagexml(self):
        pass

    def _cmake(self):
        pass

    def generate(self):
        # Load Preset
        self._header()
        self._cpp()
        self._xml()
        self._packagexml()
        self._cmake()



# class StructuRosNodelet()
# Incipit
# IfDef
# Includes
# Namespace
#   Class
#     public
#       Using
#       Funcs
#     protected
#       Variables
#     private
#       Variables
