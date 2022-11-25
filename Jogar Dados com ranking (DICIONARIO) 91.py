"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
# importou sleep para fazer o efeito de tempo
from time import sleep
# importou o itemgetter pega um item especifico
from operator import itemgetter
# randint para sorteio
from random import randint

# criou um dicionario 4 itens para sorteio
jogo = {
        'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
       }
# criou um dicionario abaixo para os itens do ranking
ranking = {}
print('Valores sorteados: ')
# fez um for para chave e valor na lista jogo em items
for k, v in jogo.items():
  # mostra chave e valor
  print(f'{k} tirou {v} no dado.')
  # sleep mostra espaçado
  sleep(1)
# faz um sorted para colocar em ordem o jogo.items()
# a chave 1 do do item da lista jogo com o itemgetter
# e o reverse é para listar reverso
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(10 * '--')
print('### Ranking ###')
# para indice em valor enumera o ranking
for i, v in enumerate(ranking):
# indice + 1, lugar e o valor 0 com o valor do dado 
  print(f'{i+1} lugar: {v[0]} com {v[1]}')
  sleep(1)
