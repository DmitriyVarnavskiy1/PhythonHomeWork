# 16	Задайте список из n чисел последовательности 〖(1+1/n)〗^n  и выведите на экран их сумму.	
# Задайте список из n чисел последовательности 〖(1+1/n)〗^n  и выведите на экран их сумму.

n = int(input("Введите число n: "))
s = 0
for i in range(1,n+1):
    s += (1+1/i)**i
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(s,2)}")