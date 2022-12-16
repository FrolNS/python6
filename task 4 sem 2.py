# ДЗ 2.4 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
#  (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

n = int(input("Введите число n: "))
newn = [i for i in range(-n, n + 1)]
# for i in range(-n, n + 1):
#     newn.append(i)
# print(newn)
with open('ДЗ 2/file.txt', 'r') as f:
    indexes = f.read().split('\n')
print(indexes)
newindexes = list(map(int, indexes))
count = 1
for i in newindexes:
    count *= newn[newindexes[i]]
print(count)