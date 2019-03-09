''' Designed for python 3.7

    Copyright 2019  Marco Treglia

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS;    OR #BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHET ER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""
'''

from gcode.primitive import exts, basename
from gcode.primitive.walker import Walker
from gcode.unit.Atoms import Mapper
from .BluePrint import BluePrint



class BluePrintManagerBase(Mapper):
        blueprints = []
        target = '.Component'

# Manager
class BluePrintManager(BluePrintManagerBase):
    def find(self):
        self.Log('Searching for Components ... ')
        for path, file in  self['files']:
                self.__add(file, path)

    def load(self):
        self.Log('Loading Components ... ')
        for blueprint in self.blueprints:
            blueprint.load()

    def produce(self):
        for blueprint in self.blueprints:
            blueprint.produce()

    def __add(self, file, path):
        if self['target'] in file:
            self.blueprints.append(BluePrint(file, path))
            self.Log(f'Add {file}', True)

    def show(self):
        self.Log(f'Current BluePrints:\n{self.blueprints}')










'''
        PREPARING RESTYLE v0.4

'''



# Agent
class Agent:
    def __init__(self, name, path=''):
        self.details = Dictionary()
        self.details[ NAME ] = name
        self.details[ BLUEPRINTS ] = path
        self.result=False

    def Log(self, emojy=None):
        result = Emoji(emojy) if emojy else LOG(self.result)
        print(f'{self.details.name}: {result} ')



# Agent ( Searcher )
class Searcher(Agent):
    def __init__(self,path='', name='Searcher'):
        super().__init__(name, path)
        self.target=None
        self.searchConfiguration()

    def searchConfiguration(self):
        for file in walker(self.details.path):
            if TARGET in file:
                self.target = file
                self.result = True
        self.Log()



# Agent ( Interpreter )
class Interpreter(Agent):
    def __init__(self, target='',name='Interpreter',):
        super().__init__(name)
        self.blueprint=None
        self.loadBluePrint(target)

    def loadBluePrint(self, target):
        ext = exts(basename(target))
        if ext in INTERPRETABLE:
            with open(target, 'r') as f:
                self.blueprint = yaml.load(f)
            self.result = True
        self.Log()



# Agent ( Generator )
class Generator(Agent):
    def __init__(self,blueprint, name='Generator'):
        super().__init__(name)



# Testing in progress

if __name__ == "__main__":

    searcher = Searcher()
    if searcher.result:
        interpreter = Interpreter(searcher.target)
        if interpreter.result:
            generator = Generator(interpreter.blueprint)
