# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
# для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные 
# варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты 
# расстановок

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

def Chess_4_options():
    start = 1
    stop = field = 8
    quantity = 1

    while quantity:
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
        if result:
            successful.append(coordinates)
            quantity -= 1
    if __name__ == '__main__':
        print(successful)

coordinates = {}
key = []
value = []
successful = []
Chess_4_options()

# import random

# def chess(vertically, horizontally):
#     res = 0
#     for v_1, h_1 in zip(vertically, horizontally):
#             for v_2, h_2 in zip(vertically, horizontally):
#                 if v_1 == v_2 or h_1 == h_2 or abs(v_1 - v_2) == abs(h_1 - h_2):
#                     res += 1
                    
#     if res > 8:
#         return False
#     else:
#         print('Ждите') 

#         return True

# coordinates = {}      
# vertically = []
# horizontally = []
# successful = []
# start = 1
# stop = 8
# quantity = 1
# filled_up = True
# horizontally_copy = []
# vertically_copy = []

# while quantity > 0:
#     while filled_up:
#         while True:
#             horizont = random.randint(start, stop)
#             if horizont not in horizontally:
#                 horizontally.append(horizont)
#             if horizontally != horizontally_copy:
#                 horizontally_copy = horizontally.copy()
#                 break
#         while True:
#             vertical = random.randint(start, stop)
#             if vertical not in vertically:
#                 vertically.append(vertical)
#             if vertically != vertically_copy:
#                 vertically_copy = vertically.copy()
#                 break
#         if len(vertically) == len(horizontally) == 8:
#             filled_up = False
    

#     options = chess(vertically, horizontally)
#     if options:
#         quantity -= 1
#         print(vertically)
#         print(horizontally)

#         for item in zip(vertically, horizontally):
#             successful.append(item)


#     if __name__ == '__main__':
#         print(options)
# print(successful)
