class Prototipo:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.__nome = nome
        self.__idade = idade
        self.__comendo = comendo
        self.__falando = falando

    def ler_dados(self):
        print(f'Olá {self.__nome}. Você tem {self.__idade} anos.')

    def comer(self, alimento):
        if self.__comendo:
            print(f'{self.__nome} já esta comendo.')
            return

        if self.__falando:
            print(f'Não pode comer falando.')
            return

        print(f'{self.__nome} come {alimento}.')
        self.__comendo = True

    def para_comer(self):
        if not self.__comendo:
            print(f'{self.__} não está comendo.')

        print(f'{self.__nome} parou de comer.')
        self.__comendo = False

    def falar(self, assunto):
        if self.__falando:
            print(f'{self.__nome} já esta falando.')
            return

        if self.__comendo:
            print(f'Não pode falar comendo.')
            return

        print(f'{self.__nome} começou a falar sobre {assunto}.')
        self.__falando = True

    def parar_falar(self):
        if not self.__falando:
            print(f'{self.__nome} não esta falando.')

        print(f'{self.__nome} parou de falar.')
        self.__falando = False


