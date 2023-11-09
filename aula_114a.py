# Função reduce()

# Aplica uma função que recebe os dois primeiros elementos de uma sequência. Em seguida, usando o próximo elemento da
# sequência, aplica novamente a função dessa vez utilizando o resultado da aplicação anterior, e assim até o fim
# dos elementos

# reduce(função, sequência, valor inicial) -> valor
# Pode-se opcionalmente determinar um valor inicial para a funcção começar

from functools import reduce

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(lambda x, y: x + y, lista_numeros))  # Está função retorna um valor e não um objeto como as anteriores
# Exemplo sem determinar valor inicial

print(reduce(lambda x, y: x + y, lista_numeros, 100))
# Exemplo estabelecendo valor inicial


# Cálculo de fatorial com a função reduce

fatorial = lambda n: reduce(lambda x, y: x*y, range(1, n+1))
# Não irá funcionar para o zero

print(fatorial(5))
