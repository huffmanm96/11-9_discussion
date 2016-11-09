from util import utilidades
from model.Humano import Humano
from model.Campo import Campo
from model.Tabuleiro import Tabuleiro
import view.Gui

'''
# Definicao de uma Classe
class PrimeiraClasse:
    'Minha primeira classe em Python'

    def __init__(self, nome, algo):
        self.nome = nome
        self.algo = algo

    def toString(self):
        return "Nome: %s\nLista de Idiomas: %s" % (self.nome, utilidades.list2string(self.algo))
# Fim - Definição de uma classe


firstClass = PrimeiraClasse("Marcelo", ['Inglês', 'Portugues', 'Japonês'])
print(firstClass.toString())

print()

marcelo = Humano("Marcelo", 1995, 1.72, 65.0)
clone = Humano("Marcelo", 1995, 1.72, 65.0)
print(marcelo.nome)
print(marcelo.imc())
print(marcelo.idade())
if(clone.nome == marcelo.nome):
    print("%s e %s são iguais!" % (clone.nome, marcelo.nome))
else:
    print("%s e %s não são iguais!" % (clone.nome, marcelo.nome))
'''
janela = view.Gui.Janela("Campo Minado", 600, 600)
tabuleiro = Tabuleiro(9, 9)
