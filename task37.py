# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:           # Класс Worker с атребутами name, surname, position (должность), и защищенный атрибут income (доход)
    
    def __init__(self,name,surname,position,income) -> None:
        self.name = name
        self.surname = surname
        self.Position = position
        self._income = income
        pass
    def __str__(self) -> str:    
        return 'Имя сотрудника: ' + self.name + '  Фамилия: ' + self.surname + '  Должность: ' + self.Position + '  Оклад: ' + str(self._income["wage"]) + '  Премия: ' + str(self._income["bonus"])

class Position(Worker):
    def get_full_name(self):
        return self.name +' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

WorkerAleks = Position('Aleks','Bronson','Texnik',{"wage": 40000, "bonus": 15000})

print(f'Доход {WorkerAleks.get_full_name()} составляет {WorkerAleks.get_total_income()}')
print(WorkerAleks.__str__())