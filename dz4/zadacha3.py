# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

spisok = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {spisok}")
nspisok = []
[nspisok.append(i) for i in spisok if i not in nspisok]
print(f"Список из неповторяющихся элементов: {nspisok}")