#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
b = ''
n = int(input("Введите число:\n"))
while n != 0:
    b = str(n%2) + b
    n //=2
print(b)