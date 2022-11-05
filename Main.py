from Model.Individuo import *
from Crossovers.CrossoverUmPonto import *
from copy import copy

#Parâmetros para configurações do algoritmo
frase_resposta = "Buscando esta frase aqui!!!"
tamanho_populacao = 1000
taxa_crossover = 60#De 0 à 100
taxa_mutacao = 25.5#De 0 à 100
qtd_iteracoes = 100



populacao = []
for x in range(tamanho_populacao):
    populacao.append(Individuo(frase_resposta))
populacao.sort(key=lambda Individuo: Individuo.get_aptidao(), reverse=True)#ordena do maior para menor
if(populacao[0].get_aptidao() == len(frase_resposta)):
    print()
    print("Resposta encontrada de primeira (rarissimo)!")
    print(populacao[0].get_genes())
    print()
else:
    for i in range(qtd_iteracoes):
        nova_pop = crossover_um_ponto(populacao,taxa_crossover,taxa_mutacao,tamanho_populacao, frase_resposta)
        nova_pop.sort(key=lambda Individuo: Individuo.get_aptidao(), reverse=True)#ordena do maior para menor
        if(nova_pop[0].get_aptidao() == len(frase_resposta)):
            print()
            print("Resposta encontrada na geração: ",i)
            print(nova_pop[0].get_genes()," Aptidão: ",nova_pop[0].get_aptidao())
            print()
            break
        else:
            print("Melhor resposta: "+nova_pop[0].get_genes()+" Aptidão: ",nova_pop[0].get_aptidao()," Iteração: ",i)
            populacao.sort(key=lambda Individuo: Individuo.get_aptidao(), reverse=True)
            controle = 0
            while len(nova_pop) < tamanho_populacao:
                nova_pop.append(copy(populacao[controle]))
                controle+=1
            populacao.clear()
            populacao = copy(nova_pop)
            nova_pop.clear()