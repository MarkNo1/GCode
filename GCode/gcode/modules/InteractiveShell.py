from gcode.unit.system import Mapper, Mouvable, File
from gcode.primitive import exists, path
from time import sleep

class GenShell(Mouvable,Mapper):

    def help(self):
        h = '''
    GenShell v 0.1

                    Commands :  new    @PlanFile
                                            create a new .type plan
                                check  @PlanFile
                                            check existing .type plan

                                add    @Type to @PlanFile

                                ls

                                help

                                exit

                    type :     Fuctions

            '''
        self.LogInfo(h)


    def chose_folder(self):
        self.LogSucces('Select the path: ')
        for dir in self.dirs:
            self.LogInfo(dir)
        uncorrect_path = True
        while(uncorrect_path):
            path = input('path:  ')
            if exists(path):
                uncorrect_path = False
        self.go(path)


    def loop(self):
        cmd = None
        while(cmd != 'exit'):
            cmd = input('> ')

            if 'help' in cmd:
                self.help()

            if 'new ' in cmd:
                file_ = cmd.split()[-1]
                filename = f'{file_}.plan'
                file_ = File(file_ ,path(self.root, filename))
                self.LogSucces(f'{filename} Created.')
                file_.write('')

            if cmd == 'ls':
                self.walk()
                for file in self.files:
                    if '.plan' in file[1]:
                        self.LogSucces(file[1])

            if 'add ' in cmd:
                type = cmd.split()[1]
                file_ = cmd.split()[2]








if __name__ == '__main__':

    genshell = GenShell()
    genshell.help()
    genshell.chose_folder()
    genshell.loop()
