class Entity:
    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self):
        return self._name


class Human(Entity):
    def __init__(self, name: str = None, age: int = 0):
        super().__init__(name)
        self.__age = age

    @property
    def age(self):
        return self.__age


humano = Human("Alex", 10)
print(humano.age)
