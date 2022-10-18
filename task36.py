# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    # класс Road имеет защищенные атрибуты длина и ширина
    
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width
        pass

    def get_mass_of_road(self):      # Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
        return self._length * self._width * 25 * 0.05


Road1 = Road(50,100)

print('Масса асфальта необходимая для покрытия данной дороги:',Road1.get_mass_of_road(),' кг')
    