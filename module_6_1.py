class Animal:
    alive = True
    fed = False
    name = str


class Plant:
    edible = False
    name = str


class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        self.edible = food.edible
        if self.food == self.edible:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True


class Predator(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        self.edible = food.edible
        if self.food != self.edible:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True


class Flower(Plant):
    def __init__(self, name):
        self.name = name

    edible = False


class Fruit(Plant):
    def __init__(self, name):
        self.name = name

    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
