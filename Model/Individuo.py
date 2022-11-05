from random import randint, random

class Individuo():

    def __init__(self, frase_resposta="", alfabeto_caracteres="!,.:;?áÁãÃâÂõÕôÔóÓéêÉÊíQWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm1234567890 "):
        self.aptidao = 0
        self.genes = ""
        self.inicializaGenes(frase_resposta, alfabeto_caracteres)
        self.avaliacao(frase_resposta)
    def set_aptidao(self, vlr):
        self.aptidao = vlr
    def set_genes(self, g):
        self.genes = g

    def get_aptidao(self):
        return self.aptidao
    def get_genes(self):
        return self.genes

    def inicializaGenes(self, frase_resposta, alfabeto_caracteres):
        self.tamaho_frase = len(frase_resposta)
        self.res = ""
        for x in range(self.tamaho_frase):
            self.res = self.res + alfabeto_caracteres[randint(0, len(alfabeto_caracteres)-1)]
        self.set_genes(self.res)
    def avaliacao(self, frase_resposta):
        self.tamaho_frase = len(frase_resposta)
        self.pontos = 0
        for x in range(self.tamaho_frase):
            if(self.genes[x] == frase_resposta[x]):
                self.pontos+=1
        self.set_aptidao(self.pontos)
    def mutacao(self, taxa_mutacao, frase_avaliacao, alfabeto_caracteres="!,.:;?áÁãÃâÂõÕôÔóÓéêÉÊíQWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm1234567890 "):
        self.qtd_caracteres_a_mudar = 1
        if(random() <= (taxa_mutacao/100)):
            for x in range(0, self.qtd_caracteres_a_mudar):
                self.novo_genes = ""
                self.posicao_gene_para_mudar = randint(0, len(self.genes)-1)
                if(self.posicao_gene_para_mudar == len(self.genes)-1):
                    self.novo_genes = self.genes[:self.posicao_gene_para_mudar] + alfabeto_caracteres[randint(0, len(alfabeto_caracteres)-1)]
                    self.genes = self.novo_genes
                else:
                    self.novo_genes = self.genes[:self.posicao_gene_para_mudar] + alfabeto_caracteres[randint(0, len(alfabeto_caracteres)-1)] + self.genes[self.posicao_gene_para_mudar+1:]
                    self.genes = self.novo_genes
            #self.avaliacao(frase_avaliacao)
