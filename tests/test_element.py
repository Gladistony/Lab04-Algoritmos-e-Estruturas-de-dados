import sys

sys.path.append("..")

# importing
from analisador import Analisador


def test_vazio():
    lst = Analisador()
    resposta = lst.acha_sequencia([0.8], [10])
    assert resposta == [0]
    resposta = lst.acha_sequencia([0.8, 0.4], [10, 5])
    assert resposta == [0, 1]
    resposta = lst.acha_sequencia([0.5, 0.9, 0.2, 0.6], [3, 1, 4, 1])
    assert resposta == [1, 0, 3, 2]
