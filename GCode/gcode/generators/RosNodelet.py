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
from gcode.unit.base import Atom
from gcode.unit.logger import  Logger
from gcode.unit.system import  File, Dir, Mouvable
from gcode.primitive.filesystem import module_path, path, read, exists
import gcode

'''
    Ros Nodelet Component
'''

green = 6770
white = 6277

DATA = 'data'

# Path to resources
MODULE_PATH = module_path(gcode)
# Generate relative path
relative_path = lambda file :  f'{MODULE_PATH}/resources/{file}'


'''
    Resources
'''
white = 6277



class Headers(Atom):
    InterfaceHeader =  File('IComponentH', relative_path('IComponentv1.h'))
    GeneratorHeader =  File('GComponentH', relative_path('GComponentv1.h'))

class ResourcesRosNodelet(Atom):
    headers = Headers()


'''
    Variable
'''

class VariableRosNodelet(Dictionary):
    header = None
    cpp = None
    xml = None
    pkgxml = None
    cmake = None


'''
    Interface
'''

class InterfaceRosNodeletComponet(VariableRosNodelet, Dir, Mouvable):
    def __init__(self, content=None):
        super().__init__(content ['name'])
        self.package = content['package']
        self.data = content
        self.resources = ResourcesRosNodelet()

    def go_to_package(self):
        # TO-DO find roscd package
        pkg = path(self.root, self.package)
        if not exists(pkg):
            self.make_dir(pkg)
            self.go(pkg)


    def _generate_headers(self):
        includes_dir = path(self.root,'include',self.package,)
        IComponentHPath = path('Interfaces', 'IComponent.h')
        GComponentHPath = path('Interfaces', 'GComponent.h')

        self.resources.headers.InterfaceHeader.copy(IComponentHPath)
        self.resources.headers.GeneratorHeader.copy(GComponentHPath)





'''
    RosNodelet
'''

class RosNodelet(InterfaceRosNodeletComponet):

    def _cpp(self):
        pass

    def _xml(self):
        pass

    def _packagexml(self):
        pass

    def _cmake(self):
        pass

    def generate(self):
        self.go_to_package()
        self._generate_headers()
        # TO-DO
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
