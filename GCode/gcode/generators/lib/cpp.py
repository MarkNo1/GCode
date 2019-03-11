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

from gcode.primitive import Dictionary
from gcode.primitive.time import time
from gcode.unit.base import Atom
from gcode.unit.logger import Logger


class CppComponent(Atom):
    pass


class InterfaceCppMapping(Logger):


    class Incipit(CppComponent):
        def __init__(self, name, brief):
            self.name = name
            self.brief = brief

        def __str__(self):
            return f'/**************************************************************************\n\
             * \n\
             *  @file 	 GComponent{self.name}.h \n\
             *  @date 	 {time}\n\
             *  @author 	Generated using GCode (T.M. Akka) \n\
             *  @brief 	 {self.brief}\n\
             *************************************************************************/\n'


    class IfDef(CppComponent):
        def __init__(self, type, classname):
            self.type = name
            self.classname = brief

        def __str__(self, type, classname):
            return f'#ifndef __{self.type}_{self.classname}__\
                     #define __{self.type}_{self.classname}__'


    class Include(CppComponent):
        def __init__(self, package, lib):
            self.package = package
            self.lib = lib

        def __str__(self):
            return f'#include <{self.package}/{self.lib}.h>'

    class Block(CppComponent):
        def __init__(self, body):
            self.body = body

        def __str__(self):
            return f'{{ \n{self.body}\n }}'

    class Namespace(CppComponent):
        def __init__(self, name, body):
            self.name = name
            self.body = body

        def __str__(self):
            return f'namespace {self.name} {Block(self.body)};'

    class Using(CppComponent):
        def __init__(self, lib, alias=None):
            self.lib=lib
            self.alias=alias

        def __str__(self):
            return f'using {self.alias} = {self.lib};' if self.alias else f'using {self.lib};'

    class decl_function(CppComponent):
        def __init__(self, name, return_type='void', args='', body=''):
            self.name = name
            self.return_type = return_type
            self.args = args
            self.body = body

        def __str__(self):
            return f'inline {self.return_type} {self.name}({self.args}) {Block(body)}'

    class call_function(CppComponent):
        def __init__(self, name, args=''):
            self.name = name
            self.args = args

        def __str__(self):
            return f'{self.name}({self.args});'

    class decl_variable(CppComponent):
        def __init__(self, type, name, init=None ):
            self.type = type
            self.name = name
            self.init = init

        def __str__(self):
            return f'{self.type} {self.name} = {self.init};\n' if init else f'{self.type} {self.name};\n'

    class IF(CppComponent):
        def __init__(self, condition, body, else_body=None):
            self.condition = condition
            self.body = body
            self.else_body = else_body

        def __str__(self):
            return f'if ({self.condition}) {Block(self.body)} else {Block(self.else_body)};\n' if self.else_body \
                else f'if ({self.condition}) {Block(body)};'






class CppMapping(InterfaceCppMapping):
    pass



# Cpp generator

DATA = 'data'
CPP = 'cpp'


class Cpp_old:
    def __init__(self, data):
        self.details = Dictionary()
        self.details[ DATA ] = data
        self.details[ CPP ] = ''

    def generate(self):
        self.flush()
        for line in self.details.data:
            print('Line: ',line)
            for key, element in line.items():
                print('Key: ', key)
                print('Element: ',*element)
                self.details.cpp += CALL(line)

    def flush(self):
        self.details.cpp = ''


# TESTING
if __name__ == '__main__':
    data = [
        {'Incipit'  : ['Alpha','Alpha is the first component generated']},
        {'Dfunction': ['FunctionTest0','void']},
        {'Dfunction': ['FunctionTest1','void', 'bool bool_']},
        {'Dfunction': ['FunctionTest2','int', 'std::string number', 'return std::stoi(number)']},
    ]

    cpp = Cpp(data)

    print(cpp.cpp)
