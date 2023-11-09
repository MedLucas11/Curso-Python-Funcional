# Expressões geradoras

# A ideia é de uma 'list comprehension' com parênteses

gen = (i ** 2 for i in range(10000) if i % 2 == 0)  # Quadrado de todos os pares de 0-9

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Vendo o consumo de memória de funções geradoras e de um list comprehension

from sys import getsizeof

list_comprehension = [i ** 2 for i in range(10000) if i % 2 == 0]

print(f'Gerador = {getsizeof(gen)}')
print(f'List Comprehension = {getsizeof(list_comprehension)}')
