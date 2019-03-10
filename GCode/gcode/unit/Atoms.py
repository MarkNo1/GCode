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


from gcode.primitive.style import TM, Mark
from gcode.primitive.style import UseStyle
from gcode.primitive.rapid import New
from gcode.primitive.time import time, clock
from gcode.primitive.filesystem import pwd, write, mkdir, exists, exts, parent_dir
from gcode.primitive.walker import Walker
from gcode import Dictionary

'''
@ ATOM
'''

DEFAULT_STYLE_CLASS = 5173

# Styles
# new
STYLE_NEW = 6770
STYLE_REPLACE = 6849
STYLE_NOTHING = 6277


class Atom(Dictionary):
    license = license
    root = pwd()
    born = time()
    class_style = DEFAULT_STYLE_CLASS

    def go(self, path):
        self['root'] = path


class Logger(Atom):
    def Log(self, text, status=None):
            to_print = f'{clock()}:{UseStyle( self.class_style ,self._class_)} '
            if status is None:
                to_print += f'{text}'
            elif isinstance(status, bool):
                to_print += f'{text} {Mark(status)}'
            elif isinstance(status, int):
                to_print += UseStyle(status, text)
            elif isinstance(status, list) and isinstance(text, list):
                for t,s in zip(text,status):
                    to_print += UseStyle(s,f'{t}')

            print(to_print)


class Mapper(Logger):
    files = walker = Walker().start().files
    dirs = walker = Walker().start().dirs


'''
    Builder
'''
class InterfaceBuilder(Logger):

    # New file
    def _new_file(self, file, content=''):
        log = ''
        if not exists(file):
            write(file, content)
            log = f'File created: {UseStyle(STYLE_NEW, file)}'
        else:
            write(file, content)
            log = f'File replaced: {UseStyle(STYLE_REPLACE, file)}'
        self.Log(log)

    # New Dir
    def _new_dir(self, dir):
        log = f'Directory already exist: {UseStyle(STYLE_NOTHING, dir)}'
        if not exists(dir):
            mkdir(dir)
            log = f'Directory created: {UseStyle(STYLE_NEW, dir)}'
        self.Log(log)


    # Safe new
    def _safe_new_file(self, file, content=''):
        dir = parent_dir(file)
        self._new_dir(dir)
        self._new_file(file, content)



class Builder(InterfaceBuilder):
    def new(self, x, content=''):
        if exts(x):
            self._safe_new_file(x, content)
        else:
            self._new_dir(x)
