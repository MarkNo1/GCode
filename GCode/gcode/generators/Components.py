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
from gcode.primitive.filesystem import module_path, path, read

import gcode.generators as gg

SUPPORTED_MODE = ['RosNodelet']


# Componet Variables
RESOURCES = 'resources'
DATA = 'data'
MODE = 'mode'
HEADERs = 'headers'
CPPs = 'cpps'
XMLs = 'xmls'
PKGXML = 'packagexml'
CMAKE = 'cmake'


'''
    Component
'''
class Component(Builder):
    def __init__(self, content=None):
        super().__init__()
        self[ DATA ] = content
        # self.go(content[''])

    def _working_dir(self):
        pass



'''
    Interface RosNodelet
'''
class InterfaceRosNodelet(Component):
    def __init__(self, content):
        super().__init__()
        self[ RESOURCES ] = Dictionary()
        self[ DATA ] = content
        self[ MODE ] = None
        self[ HEADERs ] = None
        self[ CPPs ] = None
        self[ XMLs ] = None
        self[ PKGXML ] = None
        self[ CMAKE ] = None



    def _load_resources(self):
        gen_path = module_path(gg)
        self.resources['IComponentHeader'] = read(path(gen_path, 'resources', 'IComponent.0.1.h'))
        

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
