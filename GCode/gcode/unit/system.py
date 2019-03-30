from .logger import Logger
from gcode.primitive.walker import Walker
from gcode.primitive.filesystem import pwd, module_path, path, write, read, exists, parent_dir, mkdir

'''
    MOUVABLE
'''
class Mouvable(Logger):
    def go(self, path):
        self['root'] = path
        self.LogInfo(f'Go {path}')


'''
    DIRECTORY
'''
class Dir(Logger):
    def make_dir(self, dir):
        if not exists(dir):
            mkdir(dir)
            self.Log(f'Directory created: {dir}', True)
            return None
        # self.LogWarn(f'Directory already exist {dir}')

    def dir_validator(self, file):
        dir = parent_dir(file)
        self.make_dir(dir)


'''
    FILE
'''
class File(Dir):
    def __init__(self, name, path):
        super().__init__(name)
        self.name = name
        self.root = path
        self.__exists()

    def write(self, content):
        self.dir_validator(self.root)
        self.__exists()
        write(self.root, content)
        if self.exist:
            self.LogWarn(f'Replaced: {self.root}')
        else:
            self.Log(f'Writed: {self.root}', True)

    def read(self):
        if not self.exist:
            self.LogError(f'File not exist: {self.root}')
            return None
        self.Log(f'Read: {self.root}', True)
        return read(self.root)

    def __exists(self):
        self.exist = exists(self.root)
        return self.exist

    def get_file_name(self):
        return self.root.split('/')[-1]

    def copy(self, path):
        self.write(read(path))

    def __str__(self):
        return self.read()


'''
    MAPPER
'''
class Mapper(Logger):
    def __init__(self, target='',  path=pwd()):
        super().__init__(target)
        self.root = path
        self.walk()

    def walk(self):
        self.Log(f'Starting walk in: {self.root}')
        w = Walker(self.root).start()
        self.files = w.files
        self.dirs  = w.dirs
