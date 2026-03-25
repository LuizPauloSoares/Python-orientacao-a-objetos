class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("O veículo está em movimento.")
    
class Carro(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def abrirPortaMalas(self):
        print(f"O porta-malas do {self.modelo} foi aberto com sucesso.")

class moto(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def empinar(self):
        print(f"A moto {self.modelo} está realizando uma manobra esportiva.")

class caminhao(Veiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def carregarCarga(self):
        print(f"O caminhão {self.modelo} foi carregado com sucesso e iniciou o transporte")

carro1 = Carro("Toyota", "Corolla")
moto1 = moto("Honda", "CB 500")
caminhao1 = caminhao("Volvo", "FH 540")

carro1.mover()            
carro1.abrirPortaMalas()   

moto1.empinar()         

caminhao1.carregarCarga()