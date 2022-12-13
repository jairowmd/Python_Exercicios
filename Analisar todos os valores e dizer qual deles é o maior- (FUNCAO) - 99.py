"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
# Biblioteca para timer
from time import sleep

# funcao para analisar o maior e o menor
def maior(* num):
  cont = 0
  maior = 0
  print(15 * '=-')
  print('Analisando os valores passados...')
  print(15 * '=-')
  sleep(1)
  # para valor em numero que sao os valores enviados no maior
  for valor in num:
     print(f'{valor} ', end='', flush=True)
  # descobrir o maior numero
     if cont == 0:
        maior = valor
     else:
       if valor > maior:
         maior = valor
    # contar quantos valores na funcao
     cont = cont + 1
  print(f'totalizando {cont} valores')
  print(f'o maior valor informado foi {maior}')


maior(1, 3, 4)
maior(234, 3)
maior(1, 3, 4, 344, 564, 23)
