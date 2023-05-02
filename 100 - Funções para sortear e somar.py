"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.

"""
# importa random para o sorteio da lista
from random import randint
from time import sleep

def sorteia(lista):
# para contador no range de 0 a 5 a lista vai ter 5 itens
  print('Sorteando 5 valores da lista:', end=' ')
  for cont in range(0, 5):
# acrecente na lista os numeros aleatoreos de 1 a 10
    n = randint(1, 10)
    lista.append(n)
    print(f'{n} ', end ='', flush=True)
    sleep(0.3)
  print('\nPRONTO!')

# função para somar numeros pares
def somaPar(lista):
# define soma como 0
  soma = 0
  #  se o valor for divisivel por 2 entao soma na variavel soma
  for valor in lista:
    if valor % 2 == 0:
         soma += valor
  print(f'somando os valores pares de {lista} temos {soma}')
      

numeros = list()
sorteia(numeros)
somaPar(numeros)
