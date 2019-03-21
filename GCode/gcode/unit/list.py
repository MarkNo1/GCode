from .base import Atom


class List(Atom):
    def __init__(self, name='', data=[]):
        super().__init__(name)
        self.__init(data)

    def __init(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            self.data = [data]

    def __call__(self):
        for var in self.data:
            yield var

    def __len__(self):
        return len(self.data)

    def __str__(self):
        text = ''
        for line in self.data:
            text += f'{line} '
        return text

    def add(self, val):
        self.data.append(val)
        return self

    def get_last(self):
        return self.data[-1]
