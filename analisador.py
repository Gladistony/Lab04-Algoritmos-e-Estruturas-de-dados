class Analisador:
    def __init__(self):
        pass

    def acha_sequencia(self, probs, valores) -> int:
        tamanho = len(valores)
        possibilidades = self.gerar_sequencia(tamanho) 
        melhorOrdem = possibilidades[0] 
        melhorResultado = self.calcularTotalGanhos(probs, valores, melhorOrdem)
        for o in possibilidades:
            resultado = self.calcularTotalGanhos(probs, valores, o)
            if resultado > melhorResultado:
                melhorResultado = resultado
                melhorOrdem = o
        return melhorOrdem


    def calcularTotalGanhos(self, probs, valores, ordem) -> int:
        resultado = 0
        for i in range(len(ordem)):
            prod = 1
            chance = 1
            soma = 0
            for j in range(i+1):
                prod *= probs[ordem[j]]
                soma += valores[ordem[j]]
            prod = round(prod, 3)
            id = i+1
            if id < len(ordem):
                chance = 1 - probs[ordem[id]]
            chance = round(chance, 3)
            coef = round(prod*chance, 3)
            resultado += coef * soma
        return round(resultado, 3)
    def gerar_sequencia(self, tamanho):
        self.resultados = []
        self.gerar_sequencias_rec(tamanho)
        return self.resultados
    def gerar_sequencias_rec(self, tamanho, sequencia=[], usados=[]):
        if len(sequencia) == tamanho: 
            self.resultados.append(sequencia.copy()) 
        else:
            for id in range(tamanho): 
                if id not in usados: 
                    sequencia.append(id) 
                    usados.append(id)
                    self.gerar_sequencias_rec(tamanho, sequencia, usados) 
                    sequencia.pop() 
                    usados.remove(id) 
        return self.resultados 