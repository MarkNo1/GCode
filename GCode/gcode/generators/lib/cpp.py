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

class CppD2D(Dictionary):
    pass

class CppOld:

    @staticmethod
    def incipit(file_name, author, brief):
        import datetime
        now = datetime.datetime.now()
        stars = '*' * 77 + '/\n'
        carry_on = '/*!'
        file_ = '\n*  @file \t {}'.format(file_name)
        date_ = '\n*  @date \t ' + now.strftime("%Y.%m.%d")
        author_ = '\n*  @author \t {}'.format(author)
        brief_ = '\n*  @brief \t {}'.format(brief)
        return '/' + stars + carry_on + file_ + date_ + author_ + brief_ + '\n' + stars

    @staticmethod
    def include(lib, message):
        if '.h' in message:
            message = message.split('.')[0]
        return '#include <{0}/{1}.h>'.format(lib, message)

    @staticmethod
    def declare_function(name, arguments, body, return_type):
        return 'inline {0} {1}({2}){{\n{3}\n}}'.format(return_type, name, arguments, body)

    @staticmethod
    def call_function(name, arguments):
        return '{}({});'.format(name, arguments)

    @staticmethod
    def declare_variable(type, name, initizalization=None):
        if initizalization:
            return '{} {} = {};\n'.format(type, name, initizalization)
        else:
            return '{} {};\n'.format(type, name)

    @staticmethod
    def declare_if(condition, body, body_else=None):
        if body_else:
            return 'if ({0}) {{\n{1}\n}}\nelse{{{2}\n}};\n'.format(condition,body,body_else)
        else:

            return 'if ({}) {\n{}\n};\n'.format(condition, body)

    @staticmethod
    def cast_to_string(param_name, param_type):
        return param_name if 'String' in param_type else 'std::to_string({})'.format(param_name)
