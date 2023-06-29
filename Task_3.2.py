# Дан список повторяющихся элементов. Вернуть список 
# с дублирующимися элементами. В результирующем списке 
# не должно быть дубликатов.

elements = [1, 'red', 1.123, '1.123', 23, 'blue', 1.123, 'limb', 1, 'red', 1.123]
doublon = []

def doublons(elements: list):
    for element in elements:
        if element not in doublon and elements.count(element) > 1:
            doublon.append(element)
    return doublon

print(doublons(elements))

print(list(set(elements)))
