# ДЗ 3.2
# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

listFromUser = list(input("Введите список чисел через пробел: ").split())
listInt = list(map(int, listFromUser))
print(listInt)
mult = [(listInt[i] * listInt[len(listInt) - i - 1]) for i in range((len(listInt) + 1) // 2)]
# for i in range((len(listInt) + 1) // 2):
#     mult.append(listInt[i] * listInt[len(listInt) - i - 1])
print(mult)
