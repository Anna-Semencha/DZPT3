#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

n = int(input('Введите размер списка '))
spisok = []
nspisok = []

for i in range(n):
   spisok.append(randint(0, 10))
print(spisok)

for i in range(len(spisok)):
    while i < len(spisok)/2 and n > len(spisok)/2:
        n-=1
        a = spisok[i] * spisok[n]
        nspisok.append(a)
        i += 1
print(nspisok)