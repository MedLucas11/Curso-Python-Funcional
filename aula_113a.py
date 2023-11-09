# Função filter()

# filter() aplica uma função em todos os itens de uma sequência. Se a aplicação da função em determinado item retornar
# True, este item fará parte da sequência resultante

# Caso a aplicação da função em outro determinado item retorne False, este não fará parte da sequência resultante

# A sequência resultante tem sempre o mesmo tipo que a sequência original

maior_que_tres = filter(lambda x: x > 3, [0, 1, 2, 3, 4, 5])
print(list(maior_que_tres))  # Mesma propriedade de retornar objeto que a função map()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = filter(lambda x: x % 2, numeros)  # Os valores pares retornam 0 na função módulo, sendo 0 lido como False
print(list(impares))


# Qualquer iterável pode ser utilizado, como dicionários:

lista_pessoas = [
    {'nome': 'José', 'idade': 28},
    {'nome': 'Adriana', 'idade': 39},
    {'nome': 'Pedro', 'idade': 50},
    {'nome': 'Maria', 'idade': 23},
    {'nome': 'Roberto', 'idade': 15}
]

# Menores de idade:
menores = list(filter(lambda pessoa: pessoa['idade'] < 18, lista_pessoas))
print(menores)
print(f'{menores[0]["nome"]} é menor de idade')

# Pessoas com mais de 5 letras no nome
nomes_grandes = filter(lambda pessoa: len(pessoa['nome']) > 5, lista_pessoas)
print(list(nomes_grandes))
