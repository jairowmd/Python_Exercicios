"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Obs.: aposentadoria em 35 anos de contribuição.
Com quantos anos a pessoa vai se aposentar
"""
# nome
# ano de nascimento
# carteira de trabalho
# se tiver carteira de trabalho pede ano de contratacao e pede salario e verifica quando a pessoa vai se aposentar
"""
from datetime import date
ano = 0
nasc = int(input('informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print(idade)
"""
# importado date para pegar o ano atual 
from datetime import date
ano = 0
# Dicionario vazio para o exercicio
dicionario = {}

print(15 * '-#')
print('Consulta tempo faltante para aposentar')
print(15 * '-#')
# adicionando nome e idade ao dicionario 
dicionario['nome']  = (input('Informe seu nome: '))
dicionario['idade'] = int(input('informe seu ano de nascimento: '))

# pegando o valor do ano atual
ano = date.today().year
# idade = ano - idade
idade = ano - dicionario['idade']
# dicionario idade vai receber o valor da variavel idade
dicionario['idade'] = idade

dicionario['carteira'] = int(input('informe sua carteira de trabalho (0 nao tem carteira): '))


if dicionario['carteira'] == 0:
  print(15 * '=')
  for k, v in dicionario.items():
  # mostra chave e valor
    print(f'{k} tem o valor {v}.')
    
elif dicionario['carteira'] != 0:
  dicionario['contratacao'] = int(input('informe seu ano de contratacao: '))
  dicionario['salario'] = int(input('Informe seu salario: '))
  print(15 * '=')

  # calculo qual idade a pessoa vai aposentar
  dicionario['aposentadoria'] = idade + ( (dicionario['contratacao'] + 35) - ano )
  
  print(15 * '=')
  
  for k, v in dicionario.items():
  # mostra chave e valor
     print(f'{k} tem o valor {v}.')
  print(15 * '=-')
  print('Obs.: aposentadoria em 35 anos de contribuição.') 
  print(15 * '=')
