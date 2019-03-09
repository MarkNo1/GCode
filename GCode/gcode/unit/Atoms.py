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




license = f''' Designed for python 3.7


    @1 Copyright 2019  Marco Treglia @2 1F441  Version 0.4

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS;    OR #BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHET ER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""

'''


from gcode.primitive.style import TM, LOG
from gcode.primitive.style import UseStyle
from gcode.primitive.rapid import New
from gcode.primitive.time import time
from gcode import Dictionary
from gcode.primitive.filesystem import pwd
from gcode.primitive.walker import Walker

'''
@ ATOM
'''

STYLE = Dictionary(_class=5698, _born=9924,_root=4932)

class Atom(Dictionary):
    license = license
    root = pwd()
    born = time()
    style = STYLE

    def go(self, path):
        self['root'] = path

    def __repr__(self):
        class_ = UseStyle(self['style']._class ,str(self.__class__).split('.')[-1].replace("'>", ''))
        born_ = UseStyle(self['style']._born, self.born)
        root_ =  UseStyle(self['style']._root , self.root)
        return f'{class_}|{born_}|{root_}\n'



class Logger(Atom):
    def Log(self, text, status=None):
            to_print = ''
            if status is None:
                to_print = f'{text}'
            if isinstance(status, bool):
                to_print = f'{text} {LOG(status)}'
            if isinstance(status, int):
                to_print = UseStyle(int, text)
            if isinstance(status, list) and isinstance(text, list):
                for t,s in zip(text,status):
                    to_print += UseStyle(s,f'{t}')

            print(to_print)





class Mapper(Logger):
    files = walker = Walker().start().files
    dirs = walker = Walker().start().dirs
