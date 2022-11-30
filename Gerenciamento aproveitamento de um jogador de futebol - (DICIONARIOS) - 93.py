"""
Minha solucao
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
# adicionando dicionario e lista
tot = 0
dicionario = {}
lista = []
# adicionando nome em dicionario
dicionario['nome'] = (input('Nome do Jogador: '))
# partidas vai ser uma variavel simples
partidas = int(input(f'Quantas partidas o {dicionario["nome"]} jogou ? '))

for c in range (0, partidas):
  gols = int(input(f'Quantos gols na partida {c} ? '))
  # vamos colocar gols em uma lista
  lista.append(gols)
  dicionario['gols'] = lista
  # total recebe total + gols 
  tot = tot + gols
  dicionario['total'] = tot

print(30 * '*')  
print(dicionario)
print(30 * '*')  

for k, v in dicionario.items():
  # mostra chave e valor
  print(f'O campo {k} tem o valor {v}.')

print(30 * '*') 
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas ')

# for para saber quantidade de gols em cada partida
for c in range (0, partidas):
  print(f'Na partida {c}, fez {lista[c]} gols')
  
print(f'Foi o total de {dicionario["total"]} gols')
