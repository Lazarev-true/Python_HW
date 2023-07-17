# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами 
# в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней 
# квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты 
# работы функции в json файл.

import csv
from random import randint
import os
import json

def gen_csv(list = 3, start = 1, end = 100, min_line = 100, max_line = 1000):
    with open('random_str.csv', 'w', encoding='utf-8', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows([[randint(start, end) for _ in range(list)] for _ in
                          range(randint(min_line, max_line))])

def save_json(func):
    def wrapper(*args, **qargs):
        if os.path.exists(func.__name__ + '.json'):
            with open(func.__name__ + '.json', 'r', encoding='utf-8') as res_f:
                res = json.load(res_f)
        else:
            res = []
        res.append({'variables': [*args, *qargs], 'result': (func(*args, **qargs))})
        with open(func.__name__ + '.json', 'w', encoding='utf-8') as result_f:
            json.dump(res, result_f, indent=1)
        return func
    return wrapper

def csv_variable(func):
    def wrapper(*_):
        if os.path.exists('random_str.csv'):
            with open('random_str.csv', encoding='utf-8', newline='') as res_f:
                for item in csv.reader(res_f, quoting=csv.QUOTE_NONNUMERIC):
                    func(*item)
                return func
        else:
            return func
    return wrapper

@csv_variable
@save_json
def check(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return False
    else:
        root = d ** 0.5
        x1 = (-b + root) / (2 * a)
        if d != 0:
            x2 = (-b - root) / (2 * a)
            return x1, x2
        else:
            return x1

gen_csv()
check(1, 2, 3)