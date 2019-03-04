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


## FILES & FOLDERS
import os, shutil

# Read File
read = lambda file: open(file, 'r').read()
r=read

# Write File
write = lambda file, text: open(file, 'w').write(text)
w=write

# Append File
append = lambda file, text: open(file, 'a').write(text)
a=append

# Check Existance
exists = lambda file : os.path.exists(file)
e=exists

# Is File
isFile = lambda x : os.path.isfile(x)
isf=isFile

# Is Dir
isDir = lambda x : os.path.isdir(x)
isd=isDir

# Create File
mkfile = lambda file : write(file, '') if not exists(file) else None
mf=mkfile

# Create Folder
mkdir = lambda folder : os.mkdir(folder) if not exists(folder) else None
md=mkdir

# Remove Folder
rmd = lambda folder : shutil.rmtree(folder)

# Remove File
rmf = lambda file : os.remove(file)

# General Remove
rm = lambda fd : rmf(fd) if isFile(fd) else rmd(fd)

# Joint Path
path = lambda parent, child : os.path.join(parent, child)
p=path

# List folder
list_folder = lambda path : os.listdir(path)
lsd=list_folder

# File Descriptor
file_descriptor = lambda file : open(file, 'r')
fd=file_descriptor

# Current path
pwd = lambda : os.getcwd()

# Basename
basename = lambda path : os.path.basename(path)

# File extension
exts = lambda file : file.split('.')[1]

# HD status
disk_usage = shutil.disk_usage



# Dimensions
b = 8
by = b
Kby = 1000 * by
Mby = 1000 * Kby
Gby = 1000 * Mby
Tby = 1000 * Gby
Eby = 1000 * Tby
