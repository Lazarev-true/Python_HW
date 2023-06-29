# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, 
# а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная 
# вещь отсутствует.  Для решения используйте операции с множествами. Код 
# должен расширяться на любое большее количество друзей

friends = {'Oleg': ('matches', 'food', 'tent', 'clothes'), 
           'Egor': ('food', 'water', 'barbecue', 'clothes'),
           'Roman': ('axe', 'tent', 'food', 'sleeping')}
everyone = set()

things_intersection = set.intersection(*map(set, friends.values()))
things_intersection = ', '.join(things_intersection)
print('Вещи, которые взяли все друзья:', things_intersection)
print()

for name_1, items_1 in friends.items():
    for name_2, items_2 in friends.items():
        if name_1 != name_2:
            items_1 = set(items_1) - set(items_2)
    items_1 = ', '.join(items_1)
    print(f'У друга {name_1} есть {items_1}')
print()

for name_1, items_1 in friends.items():
    for name_2, items_2 in friends.items():
        if name_1 != name_2:
            everyone.update(set(items_2))
    everyone = everyone - set(items_1)
    everyone = ', '.join(everyone)
    print(f'У всех есть {everyone}, кроме друга {name_1}')
    everyone = set()
    