from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Thalles')
print(escritor.nome)

caneta = Caneta('Pentel')
print(caneta.marca)
caneta.escrever()

maquina = MaquinaDeEscrever('Nakajima')
print(maquina.marca)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
