# Напишите функцию принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте 
# его строковое представление.

def dict_from_kwargs(**kwargs):
    result_dict = {}

    for key, value in kwargs.items():
        try:
            hash(value)
            result_dict[value] = key
        except:
            result_dict[str(value)] = key
    return result_dict

print(dict_from_kwargs(name = 'Kostik', age = 27, city = 'Orel', \
                       numbers = [35.50, 12, 37], pets = {'cat', 'dog', 'mouse'}))
