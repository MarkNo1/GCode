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

from gcode.primitive import clock
from gcode import Dictionary
from .base import Atom

# Styles
green = 6770
orange = 6849
white = 6277
red = 11023


'''
    LOGGER
'''

class InterfaceLogger(Atom):

    def __intro(self):
        c = self.use_style(self.__style__.c, self._class__)
        t =  self.use_style(self.__style__.t, self.__target__)
        return f"{clock()}: {c}.{t}" if self.__target__ else f'{clock()}: {c}'

    def _info(self, text):
        return self.use_style(white, text)

    def _warn(self, text):
        return self.use_style(orange, text)

    def _success(self, text):
        return self.use_style(green, text)

    def _error(self, text):
        return self.use_style(red, text)

    def print(self, text):
        print(f'{self.__intro()} {text}')

class Logger(InterfaceLogger):

    def LogInfo(self, text):
        self.print(self._info(text))

    def LogWarn(self, text):
        self.print(self._warn(text))

    def LogSucces(self, text):
        self.print(self._success(text))

    def LogError(self, text):
        self.print(self._error(text))


    def Log(self, text, status=None):
        if status == None:
            self.LogInfo(text)
        elif status == True:
            self.LogSucces(text)
        elif status == False:
            self.LogError(text)
        else:
            self.LogWarn(text)


    # def Log(self, text, status=None):
    #         c = UseStyle( self.class_style , self._class_)
    #         s = UseStyle( self.specialized_style , self._specialized_)
    #         name = f"{c}.{s}" if self._specialized_ else c
    #         to_print = f'{clock()}:{UseStyle( self.class_style , name)} '
    #         if status is None:
    #             to_print += f'{text}'
    #         elif isinstance(status, bool):
    #             to_print += f'{text} {Mark(status)}'
    #         elif isinstance(status, int):
    #             to_print += UseStyle(status, text)
    #         elif isinstance(status, list) and isinstance(text, list):
    #             for t,s in zip(text,status):
    #                 to_print += UseStyle(s,f'{t}')
    #
    #         print(to_print)
