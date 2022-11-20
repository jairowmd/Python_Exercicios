# DICIONÁRIOS 
# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# filme = {'titulo':'Star wars', 'ano':'1977', 'diretor':'George Lucas'}

# filme -> todos os valores - values + keys
# 'Star wars', '1977', 'George Lucas' -> values - valores do dicionarios
#  titulo,      ano,       diretor    -> keys -   keys dos dicionarios

# print(filmes.values())
# print(filmes.keys())
# print(filmes.items())

# for k, v in filme.items(): -> para cada (k) chave e valor (v) na lista filmes.items
# print('O (k) é (v)') - a KEYS É VALUES
# O primeiro resultado do for é - O (titulo) é (star wars)
# segundo - O (ano) é (1977)
# terceiro - O (diretor) é (George Lucas)

# Podemos colocar um dicionario em uma lista
#locadora = [ {'titulo':'Star wars', 'ano':'1977', 'diretor':'George Lucas'}, {'titulo':'Matrix', 'ano':'1999', 'diretor':'washovis'}]
#print(locadora[0]['ano'])
# O resultado vai ser -  1977
#print(locadora[1]['titulo']) - Matrix

#pessoas = {'nome':'Jairo', 'sexo':'M', 'idade': 28 }
#print(pessoas['idade'])
# para print formatado utilizar aspas duplas pois as simples ja sao utilizadas dentro do dicionario.
#print(f'pessoa(s) {pessoas["nome"]} tem {pessoas["idade"]}') 
#print(pessoas.keys()) - mostra o indices
# print(pessoas.values()) - valores do dicionario
# print(pessoas.items()) - indice + valores do dicionario

# mostra cada indice keys no dicionario de pessoas
#for k in pessoas.keys():
#  print(k)
#Mostrou
#nome
#sexo
#idade

# mostra os valores dos indices
#for k in pessoas.values():
#  print(k)

# para cada indice e valor em pessoas.items, mostra chave = valor
#for k, v in pessoas.items():
#  print(f'{k} = {v}')

#del pessoas['sexo'] - deleta a key sexo
#for k, v in pessoas.items():
#  print(f'{k} = {v}')

#pessoas['nome'] = 'Leandro' - substitui o item nome de Jairo para Leandro
#for k, v in pessoas.items():
#  print(f'{k} = {v}')

#pessoas['peso'] = 99  - Adiciona o item peso ao dicionario
#for k, v in pessoas.items():
#  print(f'{k} = {v}')

# criando lista e adicionando 2 dicionarios, e adicionando os dicionarios a essa lista
#brasil = []
#estado1 = {'uf':'Rio de Janeiro', 'Sigla':'RJ'}
#estado2 = {'uf':'São Paulo', 'Sigla':'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

# print(brasil[0]['uf']) - Mostra dicionario 0 a key uf

# Criando dicionario estado e lista brasil
#estado = dict()
#brasil = list()
# fazendo um laço de 3 execuções com for
#for c in range(0, 3):
# Adicionando if e sigla ao dicionario estado
#  estado['uf'] = str(input('Unidade Federativa: '))
#  estado['sigla'] = str(input('Sigla do estado: '))
# copiando para a lista brasil o dicionario estado com o comando copy()
#  brasil.append(estado.copy())
#print(brasil)



# Criando dicionario estado e lista brasil
#estado = dict()
#brasil = list()
# fazendo um laço de 3 execuções com for
#for c in range(0, 3):
# Adicionando if e sigla ao dicionario estado
#  estado['uf'] = str(input('Unidade Federativa: '))
#  estado['sigla'] = str(input('Sigla do estado: '))
# copiando para a lista brasil o dicionario estado com o comando copy()
#  brasil.append(estado.copy())
# para cada estado na sigla brasil mostra o estado - pega dicionario inteiro
#for e in brasil:
#  print(e)


# Criando dicionario estado e lista brasil
#estado = dict()
#brasil = list()
# fazendo um laço de 3 execuções com for
#for c in range(0, 3):
# Adicionando if e sigla ao dicionario estado
#  estado['uf'] = str(input('Unidade Federativa: '))
#  estado['sigla'] = str(input('Sigla do estado: '))
# copiando para a lista brasil o dicionario estado com o comando copy()
#  brasil.append(estado.copy())
# para cada estado na sigla brasil mostra o estado - pega dicionario inteiro
#for e in brasil:
#  print(e)


# Criando dicionario estado e lista brasil
# estado = dict()
#brasil = list()
# fazendo um laço de 3 execuções com for
#for c in range(0, 3):
# Adicionando if e sigla ao dicionario estado
#  estado['uf'] = str(input('Unidade Federativa: '))
#  estado['sigla'] = str(input('Sigla do estado: '))
# copiando para a lista brasil o dicionario estado com o comando copy()
#  brasil.append(estado.copy())
# para cada estado na sigla brasil mostra o estado - pega dicionario inteiro
#for e in brasil:
#  for k, v in e.items(): # para key e valor em  cada items
  # poderia declarar somente for v in e.values():
#    print(f'O campo {k} tem o valor {v}.') # printa key e valor
