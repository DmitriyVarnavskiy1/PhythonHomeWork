# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0 
    color = '' 
    name = '' 
    is_police = False

    def __init__(self, speed, color, name, is_police = False) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        pass

    def show_speed(self) -> int:
        return self.speed

    def go(self, speed) -> None: 
        if self.speed:
            print(f'машина {self.name} уже движется', end = ' ')
            if self.speed > speed:
                print('она уменьшила скорость до:', end = ' ')
            else:   
                print('она увеличила скорость до:', end = ' ')
        else:
            print(f'машина {self.name} начала движение со скоростью {speed}')
        self.speed = speed
        
    def stop(self) -> None:
        if not self.speed:
            print(f'машина {self.name} стоит на месте')
        else:
            print(f'машина {self.name} остановилась')
            self.speed = 0
    
    def turn(self, direction) -> None:
        self.direction = direction
        print(f'машина {self.name} повернула на {direction}')

class TownCar(Car):
    def show_speed(self) -> int:
        if self.speed > 60:
            print('ВНИМАНИЕ! Превышение скорости', end = ' ')
        return self.speed

class WorkCar(Car):
   def show_speed(self) -> int:
        if self.speed > 40:
            print('ВНИМАНИЕ! Превышение скорости', end = ' ')
        return self.speed

class SportCar(Car):
    def __init__(self, speed , color, name, is_police = False) -> None:
        self.is_police = False
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True) -> None:
        self.is_police = True
        super().__init__(speed, color, name, is_police)


Landcruizer = TownCar(0,'Blue','Landcruizer')
print('Скорость машины:',Landcruizer.name,' ' ,Landcruizer.show_speed())
Landcruizer.go(60)
print('Скорость машины:',Landcruizer.show_speed())
Landcruizer.turn('Улица Лермонтова')
Landcruizer.stop()

Bugatti = SportCar(120,'Red','Bugatti')
Bugatti.go(90)
print(Bugatti.show_speed())
Bugatti.turn('право')
Bugatti.stop()

Kamaz = WorkCar(50,'green','Kamaz')
Kamaz.go(70)
print(Kamaz.show_speed())
Kamaz.turn('площадь Калинина')
Kamaz.stop()

Uaz = PoliceCar(100,'White','Uaz')
Uaz.go(70)
print(Uaz.show_speed())
Uaz.turn('улица Петрова')
Uaz.stop()