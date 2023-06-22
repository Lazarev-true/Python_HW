# Напишите программу, которая принимает две строки вида “a/b” 
# - дробь с числителем и знаменателем. Программа должна 
# возвращать сумму и произведение* дробей. Для проверки 
# своего кода используйте модуль fractions.

import fractions

def lcm(x, y): 
    if x > y: 
        greater = x 
    else: 
        greater = y
    while(True): 
        if((greater % x == 0) and (greater % y == 0)): 
            lcm = greater
            break 
        greater += 1 
    return lcm 

def hcf(x, y): 
    if x > y: 
        smaller = y 
    else:
        smaller = x 
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)): 
            hcf = i
    return hcf

first = input('Введите первую строку вида “a/b” ').split('/')
second = input('Введите вторую строку вида “a/b” ').split('/')

a, b, = list(map(int, first))
c, d, = list(map(int, second))

denominator_1 = lcm(b, d)
numerator_1 = a * denominator_1 / b + c * denominator_1 / d
numerator_2 = a * c
denominator_2 = b * d

hcf_1 = hcf(int(numerator_1), denominator_1)
hcf_2 = hcf(numerator_2, denominator_2)

fraction_1 = f'{int(numerator_1 / hcf_1)}/{int(denominator_1 / hcf_1)}'
if numerator_1 % denominator_1 == 0:
    fraction_1 = int(numerator_1 / denominator_1)
fraction_2 = f'{int(numerator_2 / hcf_2)}/{int(denominator_2 / hcf_2)}'
if numerator_2 % denominator_2 == 0:
    fraction_2 = int(numerator_2 / denominator_2)

print(fraction_1)
print(fraction_2)

firstfraction = fractions.Fraction(a, b)
secondfraction = fractions.Fraction(c, d)
result_3 = firstfraction + secondfraction
result_4 = firstfraction * secondfraction

print('С помощью Fraction')
print(result_3)
print(result_4)
