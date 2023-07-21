class Animals:
    def __init__(self, name):
        self.name = name


class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def __str__(self):
        return f'Для {self.name} глубина обитания {self.depth}'


class Bird(Animals):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings
    
    def __str__(self):
        return f'Для {self.name} размах крыльев {self.wings}'
    

class Mammal(Animals):
    def __init__(self, name, coat):
        super().__init__(name)
        self.coat = coat

    def __str__(self):
        return f'Для {self.name} длина шерсти {self.coat}'
    

fish = Fish('Nemo', 20)
bird = Bird('Kesha', 15)
mammal = Mammal('Pymba', 1)

print(fish)
print(bird)
print(mammal)