# Funções Lambda

# São funções que não precisam de identificadores.
# Elas retornam o resultado "em linha"

# Estrutura: lambda 'argumentos': expressão

# Forma tradicional:
def dobro(x):
    return x*2


print(dobro(4))


# Função lambda
d = lambda x: x * 2

print(d(4))


# Podemos ter mais de 1 parâmetro:
s = lambda x, y, z: x + y + z
print(s(1, 2, 3))


# Podemos ainda fazer uma função lambda em linha, sem associar a uma variável:
print((lambda x, y, z: x + y + z)(1, 2, 3))


# Exemplo mesclando funções nomeadas e lambda
def cumprimento():
    titulo = 'Sr(a)'
    acao = lambda x: titulo + ' ' + x
    return acao


cumprimentar = cumprimento()
print(cumprimentar('Lucas'))
