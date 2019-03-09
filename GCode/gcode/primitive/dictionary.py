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

from .style import UseStyle


KEY_STYLE = 1426
VAL_STYLE = 5331


## Dictionary Extension
class Dictionary(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
        self._class_ = str(self.__class__).split('.')[-1].replace("'>", '')

    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        try:
            return self.__getattribute__(key)
        except Exception as e:
            pass

    def __call__(self, *args, **kwargs):
        if args:
            self[args]=args
        if kwargs:
            for type, val in kwargs.items():
                self[type]=val

    def __getattr__(self, key):
        if key in self:
            dict.__getattr__(self, key)

    def __repr__(self):
        to_print = ''
        incipit = '\n'
        for key, val in self.__dict__.items():
            if key !='class_':
                incipit='\n\t'
            key_ = UseStyle(KEY_STYLE , key)
            val_ = UseStyle(VAL_STYLE , val)
            to_print += f'{incipit}{key_}: {val_}'
        return to_print

    __version__ = 0.4

# Fresh
Dict = Dictionary
