from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass


class Cartao(Pagamento):
    
    def pagar(self, valor):
        return f"Pagamento feito no cartão no valor de R$ {valor:.2f}"


class Pix(Pagamento):

    def pagar(self, valor):
        return f"Pagamento feito no PIX no valor de R$ {valor:.2f}"


class Boleto(Pagamento):

    def pagar(self, valor):
        return f"Pagamento feito no boleto no valor de R$ {valor:.2f}"





def main():

    p1 = Cartao()
    print(p1.pagar(60))

    p2 = Pix()
    print(p2.pagar(60))

    p3 = Boleto()
    print(p3.pagar(60))

if __name__ == "__main__":
    main()