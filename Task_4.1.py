# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных 
# оканчивающихся на s (кроме переменной из одной буквы s) на None. Значения 
# не удаляются, а помещаются в одноимённые переменные без s на конце.

start = -1
stop = -6
new_dikt = {}
s = ' ^-^ '
hots = [1, 2, 3]
pet = {'cat', 'dog'}
sos = 112
string = 'I love you!'

variables = dict(list(globals().items())[start:stop:-1])

for key, value in variables.items():
    print(f'{key} = {value}')
print()

def end_s(key, value):
    global new_dikt
    if len(key) > 1 and key[-1] == 's':
        new_dikt.update({key: None})
        return f'{key[:-1]} = {value}'
    else:
        new_dikt.update({key: value})
        return f'{key} = {value}'

for key, value in variables.items():
    print(end_s(key, value))
print()

for key, value in new_dikt.items():
    print(f'{key} = {value}')
    