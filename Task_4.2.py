# Напишите функцию для транспонирования матрицы
from random import randint

array = []
size = 3

for i in range(size):
    array_1 = []
    for j in range(size):
        array_1.append(randint(0, 9))
    array.append(array_1)

for i in range(size):
    print(array[i])
print()

for i in [*zip(*array)]:
    print(list(i))
