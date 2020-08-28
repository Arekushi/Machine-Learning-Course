# Aprendendo conceitos de OOP em Python

class NumberTest:
    def __init__(self, valor: int, incremento: int):
        self.__valor = valor
        self.__incremento = incremento

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor


objeto = NumberTest(10, 1)
var = objeto.valor = 150
print(var)
