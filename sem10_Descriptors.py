class Poloshit:
    def __init__(self, myatrr) -> None:
        self.atr = myatrr
        
    
    def __set__(self, instance, value):
        # instance - экземпляр класса Worker - <__main__.Worker object at 0x000000E7FFEB8898>
        # value - присваиваемое значение, например 10 или 100 в нашем случае
        if value < 0:
            raise ValueError("Не может быть отрицательным")

        # присваиваем значение атрибуту, если оно прошло валидацию
        instance.__dict__[self.atr] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.atr]

    def __delete__(self, instance) -> None:
        del instance.__dict__[self.atr]
        
    
class MATH:
    ocenka = Poloshit('ocenka')
    def __init__(self, ocenka) -> None:
        self.ocenka = ocenka
        


first = MATH(7)
second = MATH(5)
print(first.ocenka)
print(second.ocenka)
first.ocenka = 8
print(first.ocenka)
second.ocenka = 5
print(first.ocenka)
second.ocenka = 10
print(second.ocenka)