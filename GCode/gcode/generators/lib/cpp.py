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

# Generative helpers lambdas

# CALL
CALL = lambda **kwards : [D2Cpp[key](*val) for key, val in kwards.items()]

# Incipit
incipit = lambda name, brief : f'\
/*****************************************************************************/\n\
/*! \n\
 *  @file 	 GComponent{name}.h \n\
 *  @date 	 {time}\n\
 *  @author 	Generated using GCode (M. Treglia Akka) \n\
 *  @brief 	 {brief}\n\
 *****************************************************************************/\n'

# Include
Include = lambda package, lib : f'#include <{package}/{lib}.h>'

# Declare Function
Dfunction = lambda name, return_type='', args='', body='' : f'\
inline {return_type} {name}({args}){{\n {body} \n}}\n'

# Call Function
Cfunction = lambda name, args='' : f'{name}({args});\n'

# Declare Variable
Dvariable = lambda type, name, init=None : f'\
{type} {name} = {init};\n' if init else f'{type} {name};\n'

# IF
If = lambda condition, body, else_body=None: f'\
if ({condition}) {{\n{body}\n}}\nelse{{{body_else}\n}};\n' if else_body \
else f'if ({condition}) {{\n{body}\n}}\n;'


# Dictionary to lambda
D2Cpp = Dictionary(
        Include   = Include,
        Dfunction = Dfunction,
        Cfunction = Cfunction,
        Dvariable = Dvariable,
        If = If)


# Cpp generator

DATA = 'data'
CPP = 'cpp'


class Cpp:
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
                print('Element',*element)
                self.details.cpp += D2Cpp[key](*element)

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
