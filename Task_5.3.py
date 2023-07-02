# Создайте функцию генератор чисел Фибоначчи

def fibonacci(n: int):
    first, second = 1, 1
    for i in range(n):
        if i == 0:
            yield first
        elif i == 1:
            yield second
        else:
            first, second = second, first + second
            yield second

n = int(input('Сколько чисел Фибоначчи вывести? '))

print(*fibonacci(n))
