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
from gcode.generators.Cpp.handler import Handler
from gcode.generators.Cpp import *

Tag = 'Internal'

pub_functions = [ DeclareFunction('Parameters', pre='virtual', post='final'),
                DeclareFunction('Topic', pre='virtual', post='final'),
                DeclareFunction(f'Callback{MSG}',args=f'const std_msgs::bool & msg'),
                DeclareFunction('Initialize', pre='virtual', post='= 0'),
                DeclareFunction('void', "Test", pre='virtual', args='bool &test', post='= 0')]
priv_functions = [DeclareFunction('void', "Test", pre='virtual', args='bool &test', post='= 0')]
prot_functions = [DeclareFunction('void', "Test1", pre='virtual', args='bool &test', post='= 0')]
header_content = [Using('future::IComponent'),
                NameSpace('generated'),
                Class(GCName, ICName).adds_public(pub_f).adds_protected(proc_f).adds_private(priv_f)]



def GetInternal(blueprint):
    internalHandler = Handler(f'{Tag}{blueprint.name}, Tag)
    internalHandler.header_corpus(header_content)
