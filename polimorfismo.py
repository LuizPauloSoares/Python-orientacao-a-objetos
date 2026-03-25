from abc import abstractmethod

class midia:
    @abstractmethod
    def exibir_info(self):
        return

class livro(midia):
    def __init__(self,titulo,autor,numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas =numero_paginas

    def exibir_info(self):
        return f"titulo{self.titulo} autor {self.autor}  quantidade de paginas {self.numero_paginas}"

class filme(midia):
    def __init__(self,titulo,diretor,duracao):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
        
    def exibir_info(self):
        return f"titulo{self.titulo} diretor {self.diretor} duracao {self.duracao}"
    
class musica(midia):
    def __init__(self,titulo,artista,duracao):
        self.titulo = titulo 
        self.artista = artista 
        self.duracao = duracao

    def exibir_info(self):
        return f"titulo{self.titulo}, artista {self.artista} duracao {self.duracao}"
    
def main():

    lista = [
            livro("1984","George Orwell",328),
            filme(" A Origem","Christopher Nolan",148),
            musica(" Bohemian Rhapsody","Queen",354)
            ]

    for  i in lista:        
        print(i.exibir_info())


if __name__ == "__main__":
    main()

