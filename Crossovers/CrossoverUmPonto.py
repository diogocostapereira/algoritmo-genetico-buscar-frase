from Model.Individuo import *
from Selecao.SelecaoTorneio import *
from random import randint
from math import *

def crossover_um_ponto(populacao, taxa_crossover, taxa_mutacao, tamanho_populacao, frase_resposta):
    nova_populacao = []
    for x in range(0, int((len(populacao) * (taxa_crossover/100))/2)):
        ponto_de_corte = randint(0, len(populacao[0].get_genes())-1)
        pais = selecao_por_torneio(populacao)
        filho1 = Individuo()
        filho2 = Individuo()
        gene_pai1 = pais[0].get_genes()
        gene_pai2 = pais[1].get_genes()
        gene_filho1 = gene_pai1[:ponto_de_corte+1] + gene_pai2[ponto_de_corte+1:]
        gene_filho2 = gene_pai2[:ponto_de_corte+1] + gene_pai1[ponto_de_corte+1:]
        filho1.set_genes(gene_filho1)
        filho2.set_genes(gene_filho2)
        filho1.mutacao(taxa_mutacao, frase_resposta)
        filho2.mutacao(taxa_mutacao, frase_resposta)
        filho1.avaliacao(frase_resposta)
        filho2.avaliacao(frase_resposta)
        nova_populacao.append(filho1)
        nova_populacao.append(filho2)
        pais.clear()
    return nova_populacao
