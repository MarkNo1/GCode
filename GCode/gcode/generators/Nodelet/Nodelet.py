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
from gcode.generators.Package import Package
from gcode.generators.Cpp.handler import Handler
from gcode.generators.Nodelet.Cpp import GetInterface, GetInternal, GetUser

class INodelet(Package):
    def __init__(self, blueprint):
        super().__init__(blueprint.name, blueprint.package)
        self.blueprint = blueprint
        self.__init_root()

    def __init_root(self):
        # TO-DO find roscd package
        pkg = path(self.root, self.package)
        if not exists(pkg):
            self.make_dir(pkg)
            self.go(pkg)



class Nodelet(INodelet):

    def cpp(self):
        # Interface
        self.add_handler(GetInterface(blueprint))
        # Internal
        self.add_handler(GetInternal(blueprint))
        # User
        self.add_handler(GetUser(blueprint))
