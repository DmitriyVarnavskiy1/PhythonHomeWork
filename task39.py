# Задание 5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print('У вас в руках ручка')
        
class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print('У вас в руках карандаш')

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print('У вас в руках маркер')

Pen1 = Pen
Pencil1 = Pencil
Handle_of_red = Handle
direct = {Pen1,Pencil1,Handle_of_red}
for i in direct:
    i.draw(i)