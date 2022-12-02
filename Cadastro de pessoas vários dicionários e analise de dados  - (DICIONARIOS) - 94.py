"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""

dicionario = {}
lista = []
soma = 0
media = 0
sexof = 0
resp = ''

#  executar o while para rodar ate parar com a condição break
while True:
  dicionario['nome'] = str(input('Informe seu nome: '))
# Foi adicionado um while dentro do outro para validação de erro
  while True:
    dicionario['sexo'] = str(input('Informe seu sexo [M/F]:')).upper()[0]
    if dicionario["sexo"] in 'MF':
       break 
    print('Erro de digitação, digite apenas F ou M .')
# foi feito a variavel sexof para contar quantidade de mulheres
  if dicionario['sexo'] == 'F':
          sexof = sexof + 1
   
  dicionario['idade'] = int(input('Informe sua idade: '))
# Variavel soma para somar as idades e fazer a media depois
  soma = soma + dicionario['idade']
# lista copia um copia do dicionario  
  lista.append(dicionario.copy())
  
  print(15 * '-=')
# Outro while dentro do outro para fazer validação de continuar S ou N 
  while True:
    resp = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    if resp in 'SN':
       break
    print('Erro de digitação, digite apenas S ou N .')

  if resp == 'N':
        break
  else:
      print(15 * '-=')

# conta a quantidade de pessoas com o len na lista 
print(f' {len(lista)} pessoas foram cadastradas.')
# faz a media abaixo com a soma dividido len da lista
media = soma / len(lista)
print(f'A média de idade é {media:5.2f} anos')
print(f'foram cadastradas {sexof} pessoa do sexo feminino')

# mostrar as pessoas acima da media de idade
print(' Lista das pessoas que estão acima da média de idade: ', end='')
# para pessoas na lista 
for p in lista:
# if para idade de pessoas for acima da media 
    if p["idade"] >= media:
        print('    ')
# para chave e valor em itens para pessoas
        for k, v in p.items():
# mostra chave = valor de cada pessoa com idade acima da media
            print(f'{k} = {v}; ', end='')
        print()
print('=-'*30) 
print('  Fim do programa ')
print('=-'*30)
