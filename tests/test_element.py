import sys
import random

sys.path.append("..")

# importing
from analisador import Analisador
def gerar_listas(n):
  # n é o número de termos das listas
  lista1 = []
  lista2 = []
  for i in range(n):
    # gerar um valor aleatório entre 0 e 1, excluindo os extremos
    valor1 = random.uniform(0.0001, 0.9999)
    # gerar um valor aleatório entre 1 e 10
    valor2 = random.randint(1, 10)
    # adicionar os valores às listas
    lista1.append(valor1)
    lista2.append(valor2)
  return lista1, lista2


def test_vazio():
    lst = Analisador()
    resposta = lst.acha_sequencia([0.8], [10])
    assert resposta == [0]
    resposta = lst.acha_sequencia([0.8, 0.4], [10, 5])
    assert resposta == [0, 1]
    resposta = lst.acha_sequencia([0.5, 0.9, 0.2, 0.6], [3, 1, 4, 1])
    assert resposta == [1, 0, 3, 2]

def test_vazio_nao():
    lst = Analisador()
    resposta = lst.acha_sequencia_nao_gulosa([0.8], [10])
    assert resposta == [0]
    resposta = lst.acha_sequencia_nao_gulosa([0.8, 0.4], [10, 5])
    assert resposta == [0, 1]
    resposta = lst.acha_sequencia_nao_gulosa([0.5, 0.9, 0.2, 0.6], [3, 1, 4, 1])
    assert resposta == [1, 0, 3, 2]

#Nem sempre a melhor solução é a solução gulosa

def test_final():
    lst = Analisador()
    chances, valores = gerar_listas(4)
    resposta = lst.acha_sequencia(chances, valores)
    resposta2 = lst.acha_sequencia_nao_gulosa(chances, valores)
    assert resposta == resposta2