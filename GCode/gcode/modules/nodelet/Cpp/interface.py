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
from gcode.generators import CppHandler
from gcode.generators.Cpp import *

Type = 'Interface'


def get_internal_include(blueprint):
    return f'{blueprint.package}/Internal', 'Internal.h'



def GetInterface(package_path, blueprint):
    classname = f'{Type}{blueprint.name}'
    internalHandler = CppHandler(classname, package_path, folder=Type, source=True)
    internalHandler.initialize(blueprint.name, blueprint.description)

    '''
            Definition Class Internal
    '''

    CLASS = Class(blueprint.name, classname)

    Parameters = dict(name='Parameters',
                       classname=classname,
                       returntype='void',
                       pre='virtual',
                       post='final',
                       body=['//TO-DO'])

    Topics = dict(name='Topics',
                       classname=classname,
                       returntype='void',
                       pre='virtual',
                       post='final',
                       body=['//TO-DO'])

    Initialize = dict(name='Initialize',
                       returntype='void',
                       pre='virtual',
                       post='=0',
                       body='')


    CLASS.adds_public([Using(classname,classname),
                        DeclareFunction(**Parameters),
                        DeclareFunction(**Topics),
                        DeclareFunction(**Initialize)])


    HPP = [ Include(*get_internal_include(blueprint)),
            Using('future::Internal'),
            NameSpace('generated').add(CLASS)]


    '''
            Declaration Class Internal
    '''

    CPP = [NameSpace('generated').adds([ImplementedMethod(**Parameters),
                                        ImplementedMethod(**Topics)])]



    internalHandler.header_corpus(HPP)
    internalHandler.source_corpus(CPP)

    return internalHandler
