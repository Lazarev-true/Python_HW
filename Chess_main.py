from Task_6 import Chess

coordinates = {}
start = 0
stop = field = 8
print('Введите восемь пар цифр от 1 до 8, через пробел:')
while field:
    key, value = map(int, input('-> ').split())
    if start < key <= stop and start < value <= stop:
        coordinates[key] = value
        field -= 1
    else:
        print('Введите правильно!')
result = Chess.chess(coordinates)
print(result)

# Координаты для проверки
# 1 1
# 2 7
# 3 5
# 4 8
# 5 2
# 6 4
# 7 6
# 8 3
