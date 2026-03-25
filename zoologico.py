class animal:
    def fazerSom(self):
        print("animal faz som")

class cachorro(animal):

    def fazerSom(self):
        print("Au au!")

class gato(animal):

    def fazerSom(self):
        print("Miau!")

class leao(animal):

    def fazerSom(self):
        print("Roar!")

g1 = gato()
g1.fazerSom()

c1 = cachorro()
c1.fazerSom()

l1 = leao()
l1.fazerSom()