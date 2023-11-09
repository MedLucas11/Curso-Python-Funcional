from math import pi

# Podemos utilizar funções anônimas dentro da função map()

lista = [1, 2, 3, 4, 5]

cubo = map(lambda x: x * x * x, lista)
print(list(cubo))

# A função map() permite várias sequências como parâmetros:
# map('função', seq1, seq2, ... , seqN) -> lista

# A lista gerada será composta por tuplas com N elementos, correspondendo ao i-ésimo elemento de cada sequência

lista_1 = [11, 12, 13, 14, 15]
lista_2 = [21, 22, 23, 24, 25]

soma = map(lambda x, y: x + y, lista_1, lista_2)
print(list(soma))

# Se as listas tiverem tamanhos diferentes, o resultado sem correspondência será preenchido com None
# Se for passada uma função, na dupla que não tiver correspondência a operação não será feita

lista_3 = [1, 2, 3]

subtracao = map(lambda x, y: x - y, lista_2, lista_3)  # lista_2 tem 5 elementos e a lista_3 tem 3 elementos
print(list(subtracao))  # A lista gerada tem apenas os 3 elementos em que foi possível realizar a operação


# Exemplo de função para calcular área de diferentes círculos:

def area_circulo(r):
    return pi * (r ** 2)


raios = [2.5, 5, 3.7, 8, 10]
areas = list(map(area_circulo, raios))

print(areas)

# Outro exemplo com uma lista de tuplas:
# Ajuste do preço de produtos em 5%

produtos = [('tv', 2500), ('fogão', 1240), ('rádio', 234)]

novo_preco = lambda produto: (produto[0], produto[1] * 1.05)

print(list(map(novo_preco, produtos)))


# Outro exemplo com lista de dicionários:

lista_pessoas = [
    {'nome': 'José', 'idade': 28},
    {'nome': 'Adriana', 'idade': 39},
    {'nome': 'Pedro', 'idade': 50},
    {'nome': 'Maria', 'idade': 23}
]

so_nomes = list(map(lambda dict: dict.get('nome'), lista_pessoas))
print(so_nomes)

so_idades = list(map(lambda dict: dict.get('idade'), lista_pessoas))
print(so_idades)

soma_idades = sum(so_idades)
print(soma_idades)
