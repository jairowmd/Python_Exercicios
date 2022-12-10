"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:       
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2 
c) uma contagem personalizada
"""
# importando a biblioteca sleep para mostrar numeros
# gradativamente
from time import sleep

# funcao para contar inicio, fim e de quanto em quanto
def contador(i, f, p):
  # abaixo validaçao se passo for menor que 0 passo vai multiplicar -1
  if p < 0:
    p = p * -1
# se passo for = 0 passo vai ser igual a 1
  if p == 0:
    p = 1
  print(15 * '=-')
  print(f'contagem de {i} ate {f} de {p} em {p}')
  sleep(1)


  # se inicio for menor que fim contador recebe inicio
  if i < f:
    cont = i
    # enquanto contador for menor ou igual ao fim
    while cont <= f:
      # flush = true é para o sleep funcionar
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont = cont + p
    print('FIM')
    # se nao 
  else:
    cont = i
    # enquanto contador for maior ou igual ao fim
    while cont >= f:
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont = cont - p
    print('FIM')

#programa principal - com dados
contador(1, 10, 1)
contador(10, 0, 2)
print(15 * '=-')
print('Agora é sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

