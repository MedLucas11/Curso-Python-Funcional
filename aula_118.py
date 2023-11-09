# Funções min() e max()

# Auto-explicativas, min() retorna o menor valor do iterável e max() retorna o maior valor do iterável

lista = [1, 45, 78, 9, 34, 67, 23]
tupla = (3, 56, 3, 56, 23, 1)
string = 'pyPRO - Seja um profissional Python!'

print(f'Menor da lista: {min(lista)} ; Maior da lista: {max(lista)}')
print(f'Menor da tupla: {min(tupla)} ; Maior da tupla: {max(tupla)}')
print(f'Menor da string: {min(string)} ; Maior da string: {max(string)}')

# Podemos trabalhar com keys também para explicitar o que queremos analisar

nomes = ['Adriana', 'Ronny', 'Renê', 'Marcelo', 'Tereza']
print(min(nomes))
print(max(nomes))  # Nesse caso ele compara o min e max em termos de ordem da tabela ASCII

# Se eu quero achar o menor e o maior nome em termos de COMPRIMENTO devo passar um parâmetro

print(min(nomes, key=lambda nome: len(nome)))
print(max(nomes, key=lambda nome: len(nome)))


# Outro exemplo

musicas = [
    {'título': 'Amigo', 'tocou': 4},
    {'título': 'Ai se eu te pego', 'tocou': 45},
    {'título': 'Para Sempre', 'tocou': 12},
    {'título': 'Nuvem de Lágrimas', 'tocou': 23},
    {'título': 'Papel Machê', 'tocou': 14}
]

'''print(min(musicas))
print(max(musicas))
Não são suportados'''

print(min(musicas, key=lambda musica: musica['tocou']))
print(max(musicas, key=lambda musica: musica['tocou']))
