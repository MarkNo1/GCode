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

from gcode.unit.base import Atom
from gcode.generators.package import Package
from gcode.generators.Cpp import CppHandler 
from .Cpp import GetInterface, GetInternal, GetUser
from gcode.primitive import path, exists

TemporaryPkgPath = '/home/marco/Desktop/Generated'

class INodelet(Package):
    def __init__(self, blueprint):
        super().__init__(blueprint.name, blueprint.package)
        self.LogSucces('Created.')
        self.blueprint = blueprint
        self._continue = True
        self.__init_root()



    def __init_root(self):
        # TO-DO find roscd package
        self.go(TemporaryPkgPath)
        pkg = path(self.root, self.package)
        if exists(pkg):
            self.LogWarn('Package already Exist')
            self.LogWarn('Proceed ?')
            # self._continue = input('\t\t\t\t\t[y, n] :  ')
            # self._continue = True if self._continue == 'y' else False

        if not exists(pkg):
            self.make_dir(pkg)
        self.go(pkg)




class Nodelet(INodelet):
    def __init__(self, blueprint):
        super().__init__(blueprint)
        if self._continue:
            self.LogSucces('Proced to add Component.')
            self.cpp()
        else:
            self.LogError('Operation aborted.')

    def cpp(self):
        # Interface
        self.add_handler(GetInterface(self.root, self.blueprint))
        # Internal
        self.add_handler(GetInternal(self.root, self.blueprint))
        # User
        self.add_handler(GetUser(self.root, self.blueprint))


    def xml(self):
        pass
