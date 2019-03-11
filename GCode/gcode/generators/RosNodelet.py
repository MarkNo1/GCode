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
from .lib import CppMapping
import gcode

D = Dictionary

'''
    Ros Nodelet Component
'''

DATA = 'data'

# Path to resources
MODULE_PATH = module_path(gcode)
# Generate relative path
relative_path = lambda file :  f'{MODULE_PATH}/resources/{file}'


'''
    Resources
'''
class CppHandler(Atom):
    def __init__(self, name, package, folder=None):
        super().__init__(name)
        self.name = name
        self.package = package
        # Folders path
        self.headers_path = self.__header_path(folder)
        self.sources_path = self.__source_path(folder)
        header_name = f'{self.name}.h'
        source_name = f'{self.name}.cc'
        # Header file
        self.header = File(f'{self.name}Header', path(self.headers_path, header_name))
        # Source file
        self.source = File(f'{self.name}Source', path(self.sources_path, source_name ))

    def __header_path(self, folder):
        root = path(self.package, 'include', self.package)
        if folder != None:
            root = path(root, folder)
        return root

    def __source_path(self, folder):
        root = path(self.package, 'src')
        if folder != None:
            root = path(root, folder)
        return root

    def init(self):
        self.header.write('')
        self.source.write('')

class Interface(Atom):
    header =  File('IComponentH', relative_path('IComponentv1.h'))
#
# class ResourcesRosNodelet(Atom):
#     headers = Headers()

class VariableRosNodelet(Dictionary):
    header = None
    cpp = None
    xml = None
    pkgxml = None
    cmake = None


class PackageStructure(Logger):
    def __init__(self, name, package):
        super().__init__(name)
        self.name = name
        self.package = package

        self.Cpp = D(# Interface
                     Interface=CppHandler(f'Interface{self.name}', self.package, 'Interface'),
                     # Generated
                     Generated = CppHandler(f'Generated{self.name}', self.package, 'Generated'),
                     # generated User
                     User = CppHandler(f'{self.name}', self.package))

    def initialize(self):
        self.LogInfo('Initializing Package Structure')
        for name, cppHandler in self.Cpp():
            self.Log(f'Init Cpp Handler {name}')
            cppHandler.init()

'''
    Interface
'''

class InterfaceRosNodeletComponet(VariableRosNodelet, Dir, Mouvable):
    def __init__(self, content=None):
        super().__init__(content ['name'])
        self.name = content ['name']
        self.package = content['package']
        self.data = content
        self.interface = Interface()
        self.package_structure = PackageStructure(self.name, self.package)

    def go_to_package(self):
        # TO-DO find roscd package
        pkg = path(self.root, self.package)
        if not exists(pkg):
            self.make_dir(pkg)
            self.go(pkg)


    def create_structure(self):
        self.LogInfo('Initializing component')
        self.package_structure.initialize()
        # Interface
        # XML
        # PACKAGE_XML
        # CMAKE

    def _generate_headers(self):
        # Interface
        Interface.header.write(self.interface.header.read())



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
        # Move to the working directory
        self.go_to_package()
        # Create the component structure
        self.create_structure()
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
