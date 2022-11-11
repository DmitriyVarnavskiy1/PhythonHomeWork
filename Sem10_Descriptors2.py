class SetType:
    def __init__(self, name , type1) -> None:
        self.name = name
        self.type1 = type1
    
    def __set__(self, instanse, value):
        if not isinstance(value, self.type1):
            raise ValueError(f'Несоответствие типов! тип атрибута должен быть {self.type1}')
        instanse.__dict__[self.name] = value
    def __delete__(self, instanse):
        print('Удаление данного атрибута невозможно')

class Newcifra:
    cifr1 = SetType('cifr1',int)
    name = SetType('name',str)

    def __init__(self, name, value) -> None:
        self.name = name
        self.cifr1 = value

Worker1 = Newcifra('Djim', 45)
Worker2 = Newcifra('Colin', 13)
del Worker2.cifr1
Worker3 = Newcifra('Djim', 3.45)