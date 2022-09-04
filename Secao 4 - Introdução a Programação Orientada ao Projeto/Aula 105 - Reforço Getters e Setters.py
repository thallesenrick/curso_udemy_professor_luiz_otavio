# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = RETORNA O VALOR CONFIGURADO DO SETTER (.)
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome



