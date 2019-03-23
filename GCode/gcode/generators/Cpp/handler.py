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

from gcode.generators.handler import Handler

from .header import Header
from .source import Source


class ICppHandler(Handler):
    def __init__(self, name, package_path, folder=None, source=None):
        super().__init__(name)
        self.name = name
        self.go(package_path)
        self.header = Header(name, package_path, folder)
        self.source = Source(name, package_path, folder) if source else None
        self.folder = folder



class CppHandler(ICppHandler):

    def initialize(self, classname, description):
        self.Log('Initializing.')
        if self.header:
            self.header.initialize(classname, description)
        if self.source:
            self.source.initialize(classname, description)

    def preview(self):
        self.Log(f'Preview Header')
        self.header.preview()
        self.Log(f'Source Header')
        self.source.preview()

    def generate(self):
        self.Log(f'Generating Header')
        if self.header:
            self.header.generate()
        self.Log(f'Generating Source')
        if self.source:
            self.source.generate()

    def header_corpus(self, corpus:list):
        self.header.add_corpus(corpus)

    def source_corpus(self, corpus:list):
        self.source.add_corpus(corpus)
