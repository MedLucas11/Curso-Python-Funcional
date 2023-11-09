# Funções all() e any()

# São duas funções booleanas, retornando True ou False dependendo das condições

# all() retorna True desde que todos os elementos de um iterável sejam verdadeiros ou se o iterável está vazio.

# any() retorna True se pelo menos um dos elementos do iterável é verdadeiro. Retorna False caso o iterável esteja vazio

print(all([0, 1, 2, 3, 4, 5]))

print(any([0, 1, 2, 3, 4, 5]))

print(all([1, 2, 3, 4, 5]))


# Verificar se todos os nomes de uma lista começam com a letra 'P'

nomes = ['Petrucia', 'Pedro', 'Paula', 'Piva', 'Pietra']

if all(nome[0] == 'P' for nome in nomes):
    print('Todos os nomes começam com a letra "P"')
else:
    print('Não são todos os nomes que começam com a letra "P"')
