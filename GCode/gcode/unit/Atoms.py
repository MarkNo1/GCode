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
from gcode.primitive.filesystem import pwd, read, write, mkdir, exists, exts, parent_dir
from gcode.primitive.walker import Walker
from gcode import Dictionary

'''
@ ATOM
'''

DEFAULT_STYLE_CLASS = 610

# Styles
# new
STYLE_NEW = 6770
STYLE_REPLACE = 6849
STYLE_NOTHING = 6277
STYLE_ERROR = 11023
DEFAULT_STYLE_SPEC = 6420


'''
    INTERFACE ATOM
'''
class InterfaceAtom(Dictionary):
    def __init__(self, name=''):
        super().__init__()
        self._specialized_ = self.__add_specialization(name)

    def __add_specialization(self, specialization):
        if specialization:
            if '.' in specialization:
                specialization = specialization.split('.')[0]
        return specialization

'''
    ATOM
'''
class Atom(InterfaceAtom):
    license = license
    root = pwd()
    born = time()
    class_style = DEFAULT_STYLE_CLASS
    specialized_style = DEFAULT_STYLE_SPEC


'''
    MOUVABLE
'''
class Mouvable(Atom):
    def go(self, path):
        self['root'] = path


'''
    LOGGER
'''
class Logger(Atom):
    def Log(self, text, status=None):
            c = UseStyle( self.class_style , self._class_)
            s = UseStyle( self.specialized_style , self._specialized_)
            name = f"{c}.{s}" if self._specialized_ else c
            to_print = f'{clock()}:{UseStyle( self.class_style , name)} '
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



'''
    DIRECTORY
'''
class Dir(Logger):
    def make_dir(self, dir):
        log = f'Directory already exist: {UseStyle(STYLE_NOTHING, dir)}'
        if not exists(dir):
            mkdir(dir)
            log = f'Directory created: {UseStyle(STYLE_NEW, dir)}'
        self.Log(log)

    def dir_validator(self, file):
        dir = parent_dir(file)
        self.make_dir(dir)


'''
    FILE
'''
class File(Dir):
    def __init__(self, name, path):
        super().__init__(name)
        self.name = name
        self.root = path
        self.exist()

    def write(self, content):
        self.dir_validator(self.root)
        write(self.root, content)
        self.Log(self.__log_rewrite() if self.exist else self.__log_new())

    def read(self):
        if not self.exist():
            self.Log(self.__log_error())
            return None
        self.Log(self.__log_read(), STYLE_NEW)
        return read(self.root)

    def __log_new(self):
        return f'Created: {UseStyle(STYLE_NEW, self.root)}'

    def __log_rewrite(self):
        return f'Replaced: {UseStyle(STYLE_REPLACE, self.root)}'

    def __log_error(self):
        return f'File not exist: {UseStyle(STYLE_ERROR, self.root)}'

    def __log_read(self):
        return f'Read: {self.root}'

    def exist(self):
        self.exists = exists(self.root)
        return self.exist


'''
    MAPPER
'''
class Mapper(Logger):
    files = walker = Walker().start().files
    dirs = walker = Walker().start().dirs



class List(Atom):
    def __init__(self, name='', data=[]):
        super().__init__(name)
        self.__init(data)

    def __init(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            self.data = [data]

    def __call__(self):
        for var in self.data:
            yield var

    def add(self, val):
        self.data.append(val)
        return self

    def __len__(self):
        return len(data)
