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

from .definition import *
from gcode.unit.logger import Logger
from gcode.unit.system import File
from gcode.primitive.filesystem import path
from gcode.generators.Cpp.definition import CppContent


class Hpp(CppContent):
    def __init__(self, filename:str, classname:str, description:str=''):
        begining = str(Incipit(filename, description))
        begining += str(IFdef('GENERATED', classname.upper())) + '\n'
        super().__init__(Delimiter(start=begining, trimend=';\n'))


class IHeader(File):
    def __init__(self, name, package, custom_folder):
        super().__init__(name)
        self.name = name
        self.header_name = f'{self.name}.h'
        self.package = package
        self.folder = custom_folder
        self.__init_root__()

    def __init_root__(self):
        root = path(self.package, 'include', self.package)
        if self.folder != None:
            root = path(root, self.folder)
        self.root = root



class Header(IHeader):
    def __init__(self, name, package, custom_folder=None):
        super().__init__(name, package, custom_folder)
        self.hpp = None

    def initialize(self, classname='', description=''):
        self.hpp = Hpp(self.header_name, classname, description)

    def produce(self):
        self.write(self.hpp)

    def preview(self):
        self.Log(self.hpp)

    def add_corpus(self, corpus:list):
        self.adds(corpus)
