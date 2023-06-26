# Создайте словарь со списком вещей для похода в качестве ключа 
# и их массой в качестве значения. Определите какие вещи влезут 
# в рюкзак передав его максимальную грузоподъёмность. Достаточно 
# вернуть один допустимый вариант. 

elements = {'water': 1500, 'food': 1000, 'barbecue': 550,
          'sleeping': 2100, 'clothes': 900, 'axe': 300,
          'knife': 150, 'tent': 3000, 'firewood': 1500, 
          'mat': 800, 'matches': 50, 'cauldron': 1000}
capacity = 5000
fit = []

sort_items = dict(sorted(elements.items(), key=lambda x: x[1], reverse=True))
# Для правильного заполнения рюкзака отсортировал словарь, и начал с больших чисел

for element in sort_items:
    if sort_items[element] <= capacity:
        fit.append(element)
        capacity -= sort_items[element]
print(fit)

# *Верните все возможные варианты комплектации рюкзака. Не придумал
