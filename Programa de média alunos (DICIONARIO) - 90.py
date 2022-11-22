"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
dicionario = {}

dicionario['nome']  = (input('Digite o nome do Estudante: '))
dicionario['media'] = float(input('Digite a media do Estudante: '))
print(15 * '=')
if dicionario['media'] >= 7:
  print('Estudante aprovado')
elif dicionario['media'] <= 5:
  print('Estudante esta reprovado')
else:
  print('Estudante esta em recuperação')
print(15 * '=')
print(f'O nome do Estudante é {dicionario["nome"]}')
print(f'A media do Estudante é {dicionario["media"]}')
