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

from gcode.primitive import fd
from gcode.primitive import UseStyle
from gcode import Dictionary
from gcode.unit import Logger
import yaml


NAME = 'name'
PATH = 'path'
CONTENT = 'content'
GENERATED = 'generated'


# Style
s_class = 610
s_componentname = 708

class BluePrintBase(Logger):
    def __init__(self, name, path):
        super().__init__()
        self.go(path)
        self[ NAME ] = name
        self[ CONTENT ] = None
        self[ GENERATED ] = Dictionary()


class BluePrint(BluePrintBase):

    def load(self):
        self.content = Dictionary(yaml.load(fd(self.root)))
        self.Log(f'{self.name} loaded', True )

    def generate(self):
        pass

    def __repr__(self):
        class_ = UseStyle(s_class ,self._class_)
        name_ = UseStyle(s_componentname, self.name)
        # born_ = UseStyle(self['style']._born, self.born)
        # root_ =  UseStyle(self['style']._root , self.root)
        return f'{class_} -> {name_}'
