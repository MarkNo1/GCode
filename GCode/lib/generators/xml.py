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


from lib.primitive import Dictionary

# XML Helper
indent = lambda n : n * '\t'
T = lambda n : f'\n{indent(n)}'

class Xml(Dictionary):
    def generate(self):
        self.__produce(0)
        return ''.join(self.xml)

    def __reset(self):
        self['indent']=0
        self['xml']=[]

    def __append(self, var):
        if var:
            self.xml.append(f'{T(self.indent)}{var}')

    def __attach(self, var):
        self.xml[-1] += var

    def __start_root(self):
        self.__append(f'<{self.root}' if self.args else f'<{self.root}>')

    def __end_root(self):
        self.__append(f'</{self.root}>')

    def __args(self):
        if self.args:
            [self.__attach(f' {key}={var}') for key, var in self.args.items()]
            self.__attach('>')

    def __body(self):
        self.__append(self.body)

    def __nestedXML(self):
        if self.xmls:
            for xml_data in self.xmls:
                xml_ = Xml(xml_data)
                self.__append(xml_.__produce(self.indent + 1))

    def __repr__(self):
        return f'\nXML->{super().__repr__()}'


    def __produce(self, indent=0):
        self.__reset()
        self.indent = indent

        # Start root
        self.__start_root()
        # Args
        self.__args()
        # Body
        self.__body()
        # Nested XML
        self.__nestedXML()
        # End Root
        self.__end_root()
        return ''.join(self.xml)
