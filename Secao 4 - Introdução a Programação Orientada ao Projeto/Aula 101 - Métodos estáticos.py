from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Método de Instância -> precisa receber o self, pois se refere a instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

# Método de Classe -> Não se refere a instância ("p1") em si,
    # mas referente a classe (GLOBAL)
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# Método Estático -> Como se fosse uma função normal dentro da classe,
    # usa-se a instância ("p1") ou chama pela classe, não pode usar o self
    # nem o nome da classe como no caso ("cls")
    @staticmethod
    def gera_id():
        rand = randint(10000, 99999)
        return rand


# p1 = Pessoa.por_ano_nascimento('Thalles', 2000)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())