# Функция filter() принимает два параметра. Первый — имя созданной пользователем функции, а второй — итерируемый объект (список, строка, множество, кортеж и так далее).

# Она вызывает заданную функцию для каждого элемента объекта как в цикле.
# Первый параметр — функция, содержащая условия для фильтрации входных значений. Она возвращает True или False. 
# Если же передать None, то она удалит все элементы кроме тех, которые вернут True по умолчанию.

numbers = [1, 2, 4, 5, 7, 8, 10, 11]


def filter_odd_num(in_num):     # функция, которая проверяет числа проверяет на четность
    if(in_num % 2) == 0:
        return True
    else:
        return False


flt = filter(filter_odd_num, numbers)            #  filter()  удалит все  нечетные чисела в списке
print(list(flt))

def functionfilter(finction , lst):
    Newlst = []
    for el in lst:
        if finction(el):
            Newlst.append(el)
    return Newlst

flt = functionfilter(filter_odd_num,numbers)
print(flt)