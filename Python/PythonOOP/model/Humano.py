__author__ = 'Marcelo'

ano = 2014

class Humano:

    def __init__(self, nome, nascimento, altura, peso):
        self.nome = nome
        self.nascimento = nascimento
        self.altura = altura
        self.peso = peso

    def idade(self):
        return ano - self.nascimento

    def imc(self):
        return self.peso / self.altura**2
