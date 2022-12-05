"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

O desafio 93 foi:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""
# utilizamos 2 listas e um dicionario onde vao as listas
time = list()
jogador = dict()
partidas = list()

# primeiro while para adicionar os dados 
while True:
  # clear no jogador para adicionar novos jogadores ao final do loop
  jogador.clear()
  # adiciona jogador ao dicionario
  jogador['nome'] = str(input('Nome do Jogador: '))
  # faz o total de partidas do jogador
  tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  # clear no jogador para adicionar partidas de novos jogadores ao final do loop
  partidas.clear()

  # for para verificar a quantidade de gols feitos nas partidas
  for c in range(0, tot):
      partidas.append(int(input(f'   Quantos gols na partidas {c+1}? ')))
  # copia quantidade de gols 
  jogador['gols'] = partidas[:]
  # soma do total
  jogador['total'] = sum(partidas)
  # copia dicionario jogador para lista time
  time.append(jogador.copy())

  # while para validação de continuação ou nao
  while True:
    resp = str(input(' Quer continuar ? [S/N] ')).upper()[0]
    if resp in 'SN':
      break
    print('Erro responda apenas S ou N')
  if resp == 'N':
    break
    
# fazendo o indice da lista de jogadores
print('-' * 40)
print('cod', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()

# fazendo um enumerate para pegar a lista codenome, gols e total da lista time
for k, v in enumerate(time):
  print(f'{k:>5} ', end='')
  
  for d in v.values():
    print(f'{str(d):<15} ', end='')
  print()
print('-' * 40) 

# fazendo while para selecionar jogador para mostrar os dados
while True:
  busca = int(input('Mostrar dados de qual jogador - 999 para parar: '))
  if busca == 999:
    break
  if busca >= (len(time)):
    print(f'Erro! nao existe jogador com o codigo {busca}')
  else:
  # pelo enumerate pega os dados do aproveitamento de cada jogador
    print(f'  ---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
    for i, g in enumerate(time[busca]["gols"]):
      print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
    
print('=-=-=-=-=VOLTE SEMPRE=-=-=-=-=')      
