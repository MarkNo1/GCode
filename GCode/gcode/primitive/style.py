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

from .dictionary import Dictionary


## COLORS

# All Colors Range
STYLES_ = [ dict(a=a,b=b,c=c)
            for a in range(8)
            for b in range(38)
            for c in range(48)]


# Create Color Code
StyleCode = lambda a, b, c : f'{a};{b};{c}'

# Get the Color from the Color Table
StyleCodeFromTable = lambda code : StyleCode(**code)

# Get Text with Added Color
StyledTextInternal = lambda color, text : f'\x1b[%sm {text} \x1b[0m' % (color)

# Get Style with human code
UseStyle = lambda human_code, text: StyledTextInternal(STYLES_TABLE[human_code], text)

# COLORS TABLE
STYLES_TABLE = dict( (idx,code) for idx, code in enumerate(list(map(StyleCodeFromTable, STYLES_))))

# Print all avaible styles
ShowAllStyles = lambda : print('STYLES TABLES\n\n' + ''.join([StyledTextInternal(style_code,human_code)
                        for human_code, style_code in STYLES_TABLE.items()]))


### DEFINE your commons styles:

Success = lambda text: UseStyle(13088, text)
Fail = lambda text: UseStyle(13087, text)
Warning = lambda text: UseStyle(13137, text)
Header = lambda text: UseStyle(1679, text)



#### UNICODE EMOJI

# License
TM = u"\u2122"

# Faces emoticons
faces = Dictionary(
        happy=u'\U0001F603'.encode('utf-8'),
        ops  =u'\U0001F605'.encode('utf-8'),
        ish  =u'\U0001F601'.encode('utf-8'),
        done =u'\U0001F60C'.encode('utf-8'),
        sad  =u'\U0001F614'.encode('utf-8'),
        angry=u'\U0001F621'.encode('utf-8'))

# Markers emoticons
marker = Dictionary(
        success=u'\U00002705'.encode('utf-8'),
        fail    =u'\U0000274C'.encode('utf-8'),
        question =u'\U00002753'.encode('utf-8'),
        esclamation=u'\U00002757'.encode('utf-8'))

u"\u2122"
# Add face emoticon
Emoji = lambda unicode : unicode.decode('utf-8')


# Logging

FAIL = lambda : Emoji(marker.fail)
SUCCESS = lambda : Emoji(marker.success)
LOG = lambda result : SUCCESS() if result else FAIL()
