from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('B', '2')
p4 = Pessoa('D', '4')

pessoas = [p1, p2, p3, p4]
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
print(p1)
print()
print(asdict(p1))
print(astuple(p1))