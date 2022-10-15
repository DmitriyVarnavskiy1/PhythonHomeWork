# Задать последовательность чисел. Написать программу, которая выведет список неповторяющихся
# элементов исходной последовательности

from random import randint


N = int(input('Введите длину последовательности: '))

List = []
for i in range(N):                                                    
    List.append(randint(0,10))
print(f'Сформирована последовательность из {N} элементов')
print(List)



NewList = []                                
for el in List:                             
    if List.count(el) == 1:                
        NewList.append(el)
print(NewList)

NewList = [el for el in List if List.count(el) == 1]    
print(NewList)