# Função sorted()

# Ordena um iterável, preservando os valores originais
# Sempre retorna uma LISTA
# Diferente de sort() que se aplica apenas em listas e retorna a lista original ordenada (alterada)

lista = [3, 5, 1, 8, 4, 2]
lista.sort()
print(lista)

tupla = (3, 5, 1, 8, 4, 2)
print(sorted(tupla))  # Retorna uma lista, apesar da estrutura original ser uma tupla

# Permite a inserção de certos parâmetros, como a ordem inversa

print(sorted(tupla, reverse=True))


# Exemplo mais complexo, utilizando dicionários:

musicas = [
    {'título': 'Amigo', 'tocou': 4},
    {'título': 'Ai se eu te pego', 'tocou': 45},
    {'título': 'Para Sempre', 'tocou': 12},
    {'título': 'Nuvem de Lágrimas', 'tocou': 23},
    {'título': 'Papel Machê', 'tocou': 14}
]

# Ordenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
# Em key= passamos uma função que pega os valores da chave 'tocou' para cada dicionário da lista 'musicas'
