from functools import reduce

# Função reduce() juntamente com map() e filter()

# Somar a idade de todas as pessoas menores de idade
lista_pessoas = [
    {'nome': 'José', 'idade': 16},
    {'nome': 'Adriana', 'idade': 6},
    {'nome': 'Pedro', 'idade': 12},
    {'nome': 'Maria', 'idade': 34},
    {'nome': 'Ronny', 'idade': 90}
]

menores_de_idade = list(filter(lambda pessoa: pessoa['idade'] < 18, lista_pessoas))

so_idades = list(map(lambda pessoa: pessoa['idade'], menores_de_idade))

soma_idades_menores = reduce(lambda x, y: x + y, so_idades)
print(f'A soma das idades dos menores de idade é {soma_idades_menores}')
