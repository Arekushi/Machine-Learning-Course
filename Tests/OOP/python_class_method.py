class Test:
    atributo_class = 0

    def __init__(self, name: str = None):
        self.__name = name

    def method(self):
        self.atributo_class += 1
        print("Hey, i'm a normal method", self)

    @classmethod
    def classmethod(cls):
        cls.atributo_class += 1
        print("Hey, i'm a classmethod", cls)

    @staticmethod
    def staticmethod():
        print("Hey, i'm a static method")


test1 = Test("Test1")
Test.classmethod()
print(test1.atributo_class)

test1.method()
print(test1.atributo_class)

test2 = Test("Test2")
print(test2.atributo_class)
