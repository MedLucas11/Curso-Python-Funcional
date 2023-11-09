# Testando velocidade de geradores
from time import time

# Para um generator
t_inicio = time()
generator = sum((num for num in range(1, 999_000_000)))
t_fim = time()
tempo_generator = t_fim - t_inicio

# Para uma lista com list comprehension
t_inicio = time()
lista = sum([num for num in range(1, 999_000_000)])
t_fim = time()
tempo_lista = t_fim - t_inicio

print(f'Tempo de execução com o generator: {tempo_generator}')
print(f'Tempo de execução com list comprehension: {tempo_lista}')
