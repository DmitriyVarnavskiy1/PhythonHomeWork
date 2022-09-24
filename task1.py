# Проверить, является ли одно число квадратом другого
a= int(input("A="))
b= int(input("B="))
print(f'{a} является квадратом {b}')
if a==b**2 or b==a**2:
    print('да')
else:
    print('нет')