# Super Classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando ...')


# Subclasse
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando ...')


# Subclasse
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando ...') 