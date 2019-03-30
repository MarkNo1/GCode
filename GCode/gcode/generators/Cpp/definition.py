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


from gcode.primitive.time import time
from gcode.unit.list import List
from gcode.unit.logger import Logger


AUTHOR = 'M.Treglia (AKKA)'


# Base Definition Class
class CppBase(List):
    def __init__(self):
        super().__init__()
        self.data = []



# Delimiter
class Delimiter(CppBase):
    def __init__(self, start: str = '', end: str='', trimstart:str ='', trimend:str=''):
        super().__init__()
        self.start = start
        self.end = end
        self.trimstart = trimstart
        self.trimend = trimend



# Base Block
class BaseBlock(CppBase):
    def __init__(self, delimiter:Delimiter = Delimiter()):
        super().__init__()
        self.delimiter = delimiter

    def add(self, val):
        self.data.append(f'{self.delimiter.trimstart}{val}{self.delimiter.trimend}')
        return self

    def adds(self, elements):
        for element in elements:
            self = self.add(element)
        return self


    def __str__(self):
        return f'{self.delimiter.start} {super().__str__()} {self.delimiter.end}'


class CppContentOld(BaseBlock):
    def __init__(self, classname:str, description:str=''):
        begining = str(Incipit(classname,description))
        begining += str(IFdef('GENERATED',classname.upper())) + '\n'
        super().__init__(Delimiter(start=begining, trimend=';\n'))


class CppContent(BaseBlock):
    def adds(self, elements):
        for element in elements:
            self = self.add(element)



# Gender Block
class GenderBlock(BaseBlock):
    def __init__(self, type:str = ''):
        super().__init__(delimiter=Delimiter(start=':\n', end='', trimstart='\t\t', trimend=';\n'))
        self.incipit = type

    def __str__(self):
        return f'{self.incipit}{super().__str__()}'


# Public Block
class Public(GenderBlock):
    def __init__(self):
        super().__init__('public')


# Protected Block
class Protected(GenderBlock):
    def __init__(self):
        super().__init__('protected')


# Private Block
class Private(GenderBlock):
    def __init__(self):
        super().__init__('private')



# Round Bracket
class RoundBracketBlock(BaseBlock):
    def __init__(self, incipit:str = ''):
        super().__init__(delimiter=Delimiter(start='(', end=')', trimend=','))
        self.incipit = incipit

    def __str__(self):
        return f'{self.incipit}{super().__str__()}'


# Square Bracket
class SquareBracketBlock(BaseBlock):
    def __init__(self, incipit:str = ''):
        super().__init__(delimiter=Delimiter(start='[', end=']', trimend=','))
        self.incipit = incipit

    def __str__(self):
        return f'{self.incipit}{super().__str__()}'


# Curly Bracket
class CurlyBracketBlock(BaseBlock):
    def __init__(self, incipit:str = ''):
        super().__init__(delimiter=Delimiter(start='{\n', end='}',trimstart='\t', trimend=';\n'))
        self.incipit = incipit

    def __str__(self):
        return f'{self.incipit}{super().__str__()}'



# Comment
class Comment(BaseBlock):
    def __init__(self):
        super().__init__(delimiter=Delimiter(start='', end='', trimstart='//'))


# Pretty Comment
class PrettyComment(BaseBlock):
    def __init__(self, n_stars):
        stars = '*' * n_stars
        start = f'/{stars}\n'
        end = f'{stars}/'
        super().__init__(delimiter=Delimiter(start=start,
                                             end=end,
                                             trimstart='*  ', trimend='\n'))




# Definition - start with #
class Definition(BaseBlock):
    def __init__(self):
        super().__init__(delimiter=Delimiter(start='', end='', trimstart='\n#'))


# Statement - end with ;
class Statement(BaseBlock):
    def __init__(self):
        super().__init__(delimiter=Delimiter(start='', end='', trimend=' '))



#### C++ Component


# IFDEF
class IFdef(Definition):
    def __init__(self, filegender:str='', classname:str=''):
        super().__init__()
        self.add(f'ifdef __{filegender}__{classname}__')
        self.add(f'define __{filegender}__{classname}__')



# INCIPIT
class Incipit(PrettyComment):
    def __init__(self, filename, description):
        super().__init__(50)
        self.add(f'@file\t{filename}')
        self.add(f'@data\t{time()}')
        self.add(f'@author\tGenerated using gcode by {AUTHOR}')
        self.add(f'@brief\t{description}')


# INCLUDE
class Include(Definition):
    def __init__(self, path:str='', library:str=''):
        super().__init__()
        self.add(f'include <{path}/{library}>')



# NAMESPACE
class NameSpace(CurlyBracketBlock):
    def __init__(self, namespace:str = ''):
        incipit = f'namespace {namespace}'
        super().__init__(incipit)



# USING
class Using(CppBase):
    def __init__(self, library:str='', alias:str=''):
        super().__init__()
        if alias:
            self.add(f'using {alias} = {library}')
        else:
            self.add(f'using {library}')



# DECLARE VARIABLE
class Variable(CppBase):
    def __init__(self, type:str='', name:str='', init:str=''):
        super().__init__()
        if init:
            self.add(f'{type} {name} = {init}')
        else:
            self.add(f'{type} {name}')


# DECLARE FUCTION
class DeclareFunction(BaseBlock):
    def __init__(self, returntype:str='', name:str='', args:str='',
                 pre:str='', post:str='', body=None, classname=None):
        super().__init__()
        if pre:
            self.add(pre)
        self.add(returntype)
        self.add(name)
        self.add(f'({args})')
        if post:
            self.add(post)


#ImplmenntedFunction
class ImplementedFucntion(CurlyBracketBlock):
    def __init__(self, returntype:str='', name:str='', args:str='',
                 pre:str='', post:str='', body:list=[]):
        incipit = DeclareFunction(returntype,name,args,pre)
        super().__init__(incipit)
        self.add(body)


# ImplementedMethod
class ImplementedMethod(CurlyBracketBlock):
    def __init__(self, returntype:str='', classname:str='', name:str='', args:str='',
                 pre:str='', post:str='', body:list=[]):
        method_name = f'{classname}::{name}'
        incipit = DeclareFunction(returntype,method_name,args,pre)
        super().__init__(incipit)
        self.adds(body)


# CALL FUNCTION
class CallFunction(BaseBlock):
    def __init__(self, name:str='', args:str=''):
        super().__init__()
        self.add(name)
        self.add(f'({args})')



# IF
class IF(CurlyBracketBlock):
    def __init__(self, condition:str='', body:str=''):
        super().__init__(f'if ({condition})')
        self.add(body)



# CLASS
class Class(CurlyBracketBlock):
    def __init__(self, name:str='', inheritance:str=''):
        incipit = f'class {name} '
        if inheritance:
            incipit += f'public: {inheritance}'
        super().__init__(incipit)
        self.public = Public()
        self.private = Private()
        self.protected = Protected()

    def add_public(self, element):
        self.public = self.public.add(element)
        return self

    def adds_public(self, elements):
        for element in elements:
            self.public = self.public.add(element)
        return self

    def add_protected(self, element):
        self.protected = self.protected.add(element)
        return self

    def adds_protected(self, elements):
        for element in elements:
            self.protected = self.protected.add(element)
        return self

    def add_private(self, element):
        self.private = self.private.add(element)
        return self

    def adds_private(self, elements):
        for element in elements:
            self.private = self.private.add(element)
        return self

    def __str__(self):
        self.data = []
        if len(self.public) > 0:
            self.add(self.public)
        if len(self.protected) > 0:
            self.add(self.protected)
        if len(self.private) > 0:
            self.add(self.private)
        return super().__str__()


# TESTING
if __name__ == '__main__':

    GCName = 'GTestClass'
    ICName = 'IComponent'

    MSG='std_msg::bool'


    file = CppContentOld(GCName, 'First attempt generate code.')

    # Using
    file.add(Using('future::IComponent'))
    # NameSpace
    file.add(NameSpace('generated'))

# Version 1
    # Class(GCName, ICName).add_public(Using('IComponent::IComponent'))
    #                                     .add_public(DeclareFunction('Parameters', pre='virtual', post='final'))
    #                                     .add_public(DeclareFunction('Topic', pre='virtual', post='final'))
    #                                     .add_public(DeclareFunction(f'Callback{MSG}',args=f'const std_msgs::bool & msg'))
    #                                     .add_public(DeclareFunction('Initialize', pre='virtual', post='= 0'))
    #                                     .add_private(DeclareFunction('void', "Test", pre='virtual', args='bool &test', post='= 0'))
    #                                     .add_protected(DeclareFunction('void', "Test1", pre='virtual', args='bool &test', post='= 0'))
    #                                     )
    #         )

# Version 2

    pub_f = [ DeclareFunction('Parameters', pre='virtual', post='final'),
                DeclareFunction('Topic', pre='virtual', post='final'),
                DeclareFunction(f'Callback{MSG}',args=f'const std_msgs::bool & msg'),
                DeclareFunction('Initialize', pre='virtual', post='= 0'),
                DeclareFunction('void', "Test", pre='virtual', args='bool &test', post='= 0'),
    ]

    priv_f = [DeclareFunction('void', "Test", pre='virtual', args='bool &test', post='= 0')]

    proc_f = [DeclareFunction('void', "Test1", pre='virtual', args='bool &test', post='= 0')]


    C = Class(GCName, ICName).adds_public(pub_f).adds_protected(proc_f).adds_private(priv_f)

    file.add(C)

    print(file)

    # Versione 3
    file3 = CppContentOld(GCName, 'Third attempt generate code.')

    file_content = [Using('future::IComponent'),
                    NameSpace('generated'),
                    Class(GCName, ICName).adds_public(pub_f).adds_protected(proc_f).adds_private(priv_f)]

    file3.adds(file_content)

    print(file3)
