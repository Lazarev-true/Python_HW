# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного 
# (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните 
# его из класса-фабрики.

from Seminar_10_Task_6 import Bird, Mammal, Fish


class Fabric:
    def make_animal(self, animal_type, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type):
        types = {'bird': Bird, 'mammal': Mammal, 'fish': Fish}
        return types[animal_type]


if __name__ == '__main__':
    fabric = Fabric()
    animal_fabric = fabric.make_animal('bird', 'Pin', 10)
    print(animal_fabric)
