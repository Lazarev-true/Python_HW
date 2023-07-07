# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей 
# на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 
# до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните 
# истину, а если бьют - ложь.
from random import shuffle

def chess(coordinates):
    res = 0
    for key_1, value_1 in coordinates.items():
        for key_2, value_2 in coordinates.items():
            if key_1 == key_2 or value_1 == value_2 or abs(key_1 - key_2) == abs(value_1 - value_2):
                res += 1
    if res > 8: # Т.к. значения из одного списка, то они повторяются, но не более 8 раз
        return False
    else:
        return True
    

def Random_chess():
    start = 1
    stop = field = 8

    while field:
        for i in range(start, stop + 1):
            key.append(i)
            value.append(i)
        shuffle(key)
        shuffle(value)
        for k, v in zip(key, value):
            coordinates[k] = v
        field -= 1

    result = chess(coordinates)
    if __name__ == '__main__':
        print(result)

coordinates = {}
key = []
value = []
Random_chess()
