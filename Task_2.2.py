# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

letters = '0123456789ABCDEF'
str = ''
BASE = 16

num = int(input('Введите число: '))

print(hex(num))

while num > 0:
    num, remainder = divmod(num, BASE)
    str = letters[remainder] + str
 
print(str)
