# Iteradores e Iteráveis

# Um iterável ou um iterable é um objeto que irá retornar um iterator quando a função iter() for executada

# Exemplo de iterables:
nome = 'pyPRO'
numeros = [1, 2, 3, 4, 5]

# Transformando-os em iterators

it_nome = iter(nome)
it_numeros = iter(numeros)

print(it_nome)
print(it_numeros)

print(next(it_numeros))  # O next() mostra os itens do iterator, na forma de um 'ponteiro'
print(next(it_numeros))
print(next(it_numeros))
print(next(it_numeros))
print(next(it_numeros))