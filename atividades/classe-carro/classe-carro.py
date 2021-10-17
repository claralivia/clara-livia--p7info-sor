# -*- coding: utf-8 -*-

class Carro:
    '''Classe para calcular o nível do tanque de gasolina de um carro'''
    def __init__(self, consumo):
        '''Método construtor com o consumo do carro'''
        self.consumo = consumo
    def adicionarGasolina(self, litros):
        '''Método que adiciona combustível ao tanque'''
        self.litros = litros
    def andar(self, andando):
        '''Método que calcula o combustível restante após o carro andar'''
        self.andando = andando
        self.litros = self.litros - self.andando/self.consumo
    def obterGasolina(self):
        '''Método que retorna o valor do nível do tanque em litros'''
        print('NÍVEL DO TANQUE: {:.2f} litros'.format(self.litros))

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()
