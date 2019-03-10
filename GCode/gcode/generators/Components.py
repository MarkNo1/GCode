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
from gcode.unit.Atoms import Builder
from gcode.primitive.filesystem import module_path, path, read, exists

import gcode.generators as gg

SUPPORTED_MODE = ['RosNodelet']


'''
    Component
'''

green = 6770
white = 6277

DATA = 'data'

class Component(Builder):
    def __init__(self, content=None):
        specialized = content['name']
        super().__init__(specialized)
        self[ DATA ] = content
        # self.go(content[''])
        self.Log('Created.', green)


    def _working_dir(self):
        pass

    def _load_resource_file(self, file):
        gen_path = module_path(gg)
        file_path = path(gen_path, 'resources', file)
        return self.read(file_path)



'''
    Interface Componet RosNodelet
'''

RESOURCES_ROSNODELET = Dictionary(
    headers= Dictionary(IComponent='IComponentv1.h'),

)

class InterfaceRosNodelet(Component):
    resources = Dictionary()
    mode = None
    header = None
    cpp = None
    xml = None
    pkgxml = None
    cmake = None


    def _load_resources(self):
        for type, resource in RESOURCES_ROSNODELET.iterate():
            self.resources[type] = Dictionary()
            for name, file in resource.iterate():
                self.Log(f'Loading {file}')
                self.resources[type][name] = self._load_resource_file(file)


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


'''
    RosNodelet
'''
class RosNodelet(InterfaceRosNodelet):
    def generate(self):
        # Load Preset
        self._load_resources()

        self._header()
        self._cpp()
        self._xml()
        self._packagexml()
        self._cmake()
