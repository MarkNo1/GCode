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
