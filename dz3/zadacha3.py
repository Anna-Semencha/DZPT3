#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

spisok = list(map(float, input("Введите числа через пробел:\n").split()))
nspisok = [round(i%1,2) for i in spisok if i%1 != 0]
print(nspisok)
print(round(max(nspisok) - min(nspisok),3))