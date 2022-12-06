"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


# funcao de multiplicação simples 
def calculoarea(l, c):
  area = l * c
  print('-' * 30)
  print(f'A area de um terreno de {l} x {c} é de {area} metros quadrados') 

  
# programa principal
print('-' * 30)
print('controle de terreno')
print('-' * 30)

l = float(input('Largura do terreno em metros quadrados: '))
c = float(input('Comprimento do terreno em metros quadrados: '))

calculoarea(l,c)
