from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self,
                 name: str = None):
        self._name = name

    @abstractmethod
    def speak(self):
        raise NotImplemented

    @property
    def name(self):
        return self._name


class Dog(Animal):
    def speak(self):
        print("AU AU")


class Cat(Animal):
    def speak(self):
        print("MEOW MEOW")


cat = Cat()
cat.speak()
print(cat.name)
