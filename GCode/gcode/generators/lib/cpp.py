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
from gcode.unit.list import List


class CppComponent(Atom):
    def __init__(self):
        super().__init__()


class Delimiter(Atom):
    def __init__(self, start: str = '{', end: str='}'):
        super().__init__()
        self.start = start
        self.end = end



class Block(List):
    def __init__(self, delimiter:Delimiter = Delimiter()):
        super().__init__('Body')
        self.data = []
        self.delimiter = delimiter
        self.add(f'{self.delimiter.start}\n')

    def __str__(self):
        if self.delimiter.end:
            if self.delimiter.end not in self.data[-1]:
                self.add(self.delimiter.end)
        return super().__str__()


class ClassGender(Block):
    def __init__(self, type:str = 'public'):
        super().__init__(delimiter=Delimiter(start=':', end=None))
        self.type = type

    def add(self, val):
        self.data.append(f'\t{val}')
        return self

    def __str__(self):
        return f'{self.type}{super().__str__()}'


class Public(ClassGender):
    pass


class Protected(ClassGender):
    def __init__(self):
        super().__init__('protected')


class Private(ClassGender):
    def __init__(self):
        super().__init__('private')


# Class Enum
PUBLIC = 3
PROTECTED = 4
PRIVATE = 5

class Class(Block):
    def __init__(self, name, inheritance=''):
        super().__init__()
        self.name = name
        self.inheritance = inheritance
        self.add(Public())
        self.public = self.__len__()
        self.add(Protected())
        self.add(Private())

    def add_public(self, val):
        print(self.data[PUBLIC])
        self.data[PUBLIC].add(val)
        return self

    def add_protected(self, val):
        self.data[PROTECTED].add(val)
        return self

    def add_private(self, val):
        self.data[PRIVATE].add(val)
        return self

    def __str__(self):
        class_ = f'class {self.name} '
        if self.inheritance:
            class_ += f'public: {self.inheritance}'

        return f'{class_} {super().__str__()}'



class Incipit(CppComponent):
    def __init__(self, name, brief):
        super().__init__()
        self.name = name
        self.brief = brief

    def __str__(self):
        return f'/**************************************************************************\n\
             * \n\
             *  @file 	 {self.name}.h \n\
             *  @date 	 {time()}\n\
             *  @author Generated using GCode (T.M. Akka) \n\
             *  @brief 	 {self.brief}\n\
             *************************************************************************/\n'


class IfDef(CppComponent):
    def __init__(self, type, classname):
        super().__init__()
        self.type = type
        self.classname = classname

    def __str__(self):
        return f'#ifndef __{self.type}_{self.classname}__\
                 \n#define __{self.type}_{self.classname}__'


class Include(CppComponent):
    def __init__(self, package, lib):
        super().__init__()
        self.package = package
        self.lib = lib

    def __str__(self):
        return f'#include <{self.package}/{self.lib}.h>'



class Namespace(CppComponent):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.body_block = Block()

    def add(self, element):
        self.body_block.add(element)
        return self

    def __str__(self):
        return f'namespace {self.name} {self.body_block}'



class Using(CppComponent):
    def __init__(self, lib, alias=None):
        super().__init__()
        self.lib=lib
        self.alias=alias

    def __str__(self):
        return f'using {self.alias} = {self.lib};' if self.alias else f'using {self.lib};'

class DeclareFunction(CppComponent):
    def __init__(self, name, return_type='void', args='', body='', pre='', post=''):
        super().__init__()
        self.name = name
        self.return_type = return_type
        self.args = args
        self.body = Block()
        self.pre = pre
        self.post = post

    def __str__(self):
        to_return = ''
        if self.pre:
            to_return += f'{self.pre}'
        to_return = f'{self.return_type} {self.name}({self.args})'
        if self.post:
            to_return += f'{self.post}'
        if self.block:
            to_return += f'{self.body}'
        return to_return + ';'


class Decl_Variable(CppComponent):
    def __init__(self, type, name, init=None):
        super().__init__()
        self.type = type
        self.name = name
        self.init = init

    def __str__(self):
        return f'{self.type} {self.name} = {self.init};' if self.init else  f'{self.type} {self.name};'

class Call_function(CppComponent):
    def __init__(self, name, args=''):
        super().__init__()
        self.name = name
        self.args = args

    def __str__(self):
        return f'{self.name}({self.args});'

class Decl_variable(CppComponent):
    def __init__(self, type, name, init=None ):
        super().__init__()
        self.type = type
        self.name = name
        self.init = init

    def __str__(self):
        return f'{self.type} {self.name} = {self.init};\n' if init else f'{self.type} {self.name};\n'

class IF(CppComponent):
    def __init__(self, condition, body, else_body=None):
        super().__init__()
        self.condition = condition
        self.body = body
        self.else_body = else_body

    def __str__(self):
        return f'if ({self.condition}) {Block(self.body)} else {Block(self.else_body)};\n' if self.else_body \
                else f'if ({self.condition}) {Block(self.body)};'




class Code(List):
    pass



class InterfaceCppMapping(Logger):
    def __init__(self, name):
        super().__init__(name)
        self.code = Code()

    def add(self, element):
        self.code.add(element)

    def get_last(self):
        return self.code[-1]



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

    cpp = CppMapping

    GCName = 'GTest'
    ICName = 'IComponent'

    MSG='std_msg::bool'

    GCH = CppMapping('GeneratedComponentHeader')
    # Incipit
    GCH.add(Incipit(GCName, 'First attempt generate code.'))
    # IfDef
    GCH.add(IfDef('Generated', GCName))
    # Using
    GCH.add(Using('future::IComponent'))
    # NameSpace
    GCH.add(
            Namespace('generated').add(
                Class(GCName, ICName).add_public(
                    Using('IComponent::IComponent')
                    ).add_public('public:'
                    ).add_public(DeclareFunction('Parameters', pre='virtual', post='final')
                    ).add_public(DeclareFunction('Topic', pre='virtual', post='final')
                    ).add_public(DeclareFunction(f'Callback{MSG}',args=f'const std_msgs::bool & msg')
                    ).add_public(DeclareFunction('Initialize', pre='virtual', post='= 0')
                    ).add_public('private:'
                    )
                )
            )

    C = Class(GCName, ICName)
    for i in range(10):
        C.add('Test'+ str(i))


    print(GCH.code)

    print(C)
