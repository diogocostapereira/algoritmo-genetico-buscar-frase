from Model.Individuo import *
from copy import copy
from random import randint, shuffle

def selecao_por_torneio(populacao):
    shuffle(populacao)
    while True:
        num1 = randint(0, len(populacao)-1)
        num2 = randint(0, len(populacao)-1)
        if(num1 != num2):
            break
    pais = []
    pais.append(copy(populacao[num1]))
    pais.append(copy(populacao[num2]))
    return pais
