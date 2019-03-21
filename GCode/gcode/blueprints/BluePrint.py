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

from gcode.primitive import fd, exists, mkdir, path
from gcode.primitive import UseStyle
from gcode import Dictionary
from gcode.unit.system import Mouvable
from gcode.generators.Nodelet.Nodelet import Nodelet
import yaml



class IBluePrint(Mouvable):
    def __init__(self, name, path):
        super().__init__(name)
        self.go(path)
        self.blueprint = None
        self.Log('Created.', True)

    def create_component(self):
        if self.blueprint.mode == 'Nodelet':
            self.component = Nodelet(self.blueprint)



class BluePrint(IBluePrint):

    def load(self):
        self.blueprint = Dictionary(yaml.load(fd(self.root)))
        self.Log('Configuration Loaded.', True)

    def define(self):
        self.Log('Creating Component')
        # Create the suited component
        self.create_component()

    def generate(self):
        self.Log('Generating Component')
        if self.component:
            self.component.generate()
        else:
            self.LogError('Format not supported')
