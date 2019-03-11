from .logger import Logger
from gcode.primitive.walker import Walker
from gcode.primitive.filesystem import module_path, path, write, read, exists, parent_dir, mkdir

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
        self.LogWarn(f'Directory already exist {dir}')

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
        write(self.root, content)
        if self.exist:
            self.LogWarn(f'Replace: {self.root}')
        else:
            self.Log(f'Created: {self.root}', True)

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
        backup_path = self.root
        content = self.read()
        self.root = path
        self.write(content)
        self.root = backup_path



'''
    MAPPER
'''
class Mapper(Logger):
    files = walker = Walker().start().files
    dirs = walker = Walker().start().dirs
