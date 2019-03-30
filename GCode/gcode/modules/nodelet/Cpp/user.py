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

Type = 'User'


def GetUser(package_path, blueprint):
    classname = f'{Type}{blueprint.name}'
    internalHandler = CppHandler(classname, package_path, folder=Type, source=True)
    internalHandler.initialize(blueprint.name, blueprint.description)

    # Public functions

    DInitialize = dict(name='Initialize',
                       returntype='void',
                       pre='virtual',
                       post='=0',
                       body='TO-DO')

    # Header
    public = [ Using(classname,classname),
               DeclareFunction(**DInitialize)]

    # Header class
    header_class = Class(blueprint.name, classname).adds_public(public)
    # Header corpus
    internalClass = f'Internal{blueprint.name}'
    interfacePath = f'{blueprint.package}/Interface'
    interfaceLib = f'{internalClass}.h'
    header_corpus = [Include(interfacePath, interfaceLib), Using(f'generated::{internalClass}'), NameSpace('user').add(header_class)]
    # Add header
    internalHandler.header_corpus(header_corpus)

    # Source

    # Functions
    functions = [ImplementedMethod(**DInitialize)]
    # Corpus
    source_corpus = [NameSpace('user').adds(functions)]
    # Add source
    internalHandler.source_corpus(source_corpus)

    return internalHandler
