import math

class Forma:
    def calcularArea(self):
        pass
    
class quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado*self.lado
 
class retangulo(Forma):
    def __init__(self,base,altura):
        self.base = base 
        self.altura = altura
        
    def calcularArea(self):
        return self.base*self.altura
    

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * (self.raio ** 2)


def main():

    q = quadrado(4)
    r = retangulo(5, 3)
    c = Circulo(2)
    
    lista = [q,r,c]

    for i in lista:
        print(i.calcularArea())
    
if __name__ == "__main__":
    main()
