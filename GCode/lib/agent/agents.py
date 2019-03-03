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

import yaml

from lib.primitive import walker, pwd, exts, basename
from lib.primitive import Dictionary
from lib.primitive import LOG


TARGET = 'ComponentList'

INTERPRETABLE = ['yaml']



# Agent
class Agent:
    def __init__(self, name, path=pwd()):
        self.details = Dictionary()
        self.details['name'] = name
        self.details['path'] = path
        self.result=False

    def Log(self):
        print(f'{self.details.name}: {LOG(self.result)} ')


# Agent ( Searcher )
class Searcher(Agent):
    def __init__(self,path=pwd(), name='Searcher'):
        super().__init__(name, path)
        self.target=None

        for file in walker(self.details.path):
            if TARGET in file:
                self.target = file
                self.result = True
        self.Log()


# Agent ( Interpreter )
class Interpreter(Agent):
    def __init__(self, target='',name='Interpreter',):
        super().__init__(name)
        type_ = exts(basename(target))
        self.blueprint=None

        if type_ in INTERPRETABLE:
            with open(target, 'r') as f:
                self.blueprint = yaml.load(f)
            self.result = True
        self.Log()


# Agent ( Generator )
class Generator(Agent):
    def __init__(self,blueprint, name='Generator'):
        super().__init__(name)
        self.Log()


# TESTING
searcher = Searcher()
if searcher.result:
    interpreter = Interpreter(searcher.target)
    if interpreter.result:
        generator = Generator(interpreter.blueprint)
