from abc import ABC, abstractmethod

class transporte(ABC):

    @abstractmethod
    def mover(self):
        pass

class Carro(transporte):
    def mover(self):
        return "O carro está percorrendo a estrada."

class aviao(transporte):
    def mover(self):
        return "O avião está voando em altitude de cruzeiro."

class barco(transporte):
    def mover(self):
        return "O barco está navegando pelas águas."

def main():

    v1 = Carro()
    print(v1.mover())

    v2 = aviao()
    print(v2.mover())

    v3 = barco()
    print(v3.mover())

if __name__ == "__main__":
    main()