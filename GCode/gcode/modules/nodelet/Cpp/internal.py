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
from gcode.generators.lib.cpp import *

Type = 'Internal'



def GetInternal(package_path, blueprint):
    componentName = f'{Type}{blueprint.name}'
    internalHandler = CppHandler(componentName, package_path, folder=Type)
    internalHandler.initialize(blueprint.name, blueprint.description)

    # Definint header content
    interface_class = f'Interface{blueprint.name}'
    public = [ Using(interface_class,interface_class),
               DeclareFunction('void', 'Parameters', post='final'),
               DeclareFunction('void', 'Topic', post='final'),
               DeclareFunction('void', 'Initialize', post='= 0'),
    ]

    class_ = Class(blueprint.name, interface_class).adds_public(public)


    header_corpus = [
        Using('future::IComponent'),
        NameSpace('generated').add(class_)
    ]

    internalHandler.header_corpus(header_corpus)

    return internalHandler
