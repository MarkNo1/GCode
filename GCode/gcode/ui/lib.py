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


#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

"""
PyVision for the sexylib PyQt6
last edited: March 2019
"""

import sys, traceback
from PyQt5.QtWidgets import QApplication, QWidget
from gcode import Dictionary
from gcode import Logger

# Default Windows features
DefaultWindowsGeometry = Dictionary(x=300,y=300, h=360, w=420)


# QT QApplication
class Application(Logger):
    def __init__(self, *args, **kwargs):
        super().__init__('QT')
        self.LogSucces('Start')
        self.APP = QApplication(*args,**kwargs)

    # Destructor
    def __del__(self):
        try:
            sys.exit(self.APP.exec_())
        except BaseException:
            self.Log('End')


# QT Widgets Window
def Window(geometry=DefaultWindowsGeometry):
    w = QWidget()
    w.resize(geometry.h, geometry.w)
    w.move(geometry.x, geometry.y)
    w.setWindowTitle('Simple')
    return w



if __name__ == '__main__':
    from time import sleep
    app = Application(sys.argv)
    w = Window()
    w.show()

    sleep(10)
