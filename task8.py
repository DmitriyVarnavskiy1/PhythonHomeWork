#8.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x, y = int(input("Введите координату x: ")), int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка находится в первой четверти координатной плоскости")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти координатной плоскости")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти координатной плоскости")
elif x > 0 and y < 0:
    print("Точка находится в четвертой четверти координатной плоскости")
elif x == 0:
    print("Точка на оси Y")
else:
    print("Точка на оси X")