# Lazy Evaluation

# Recurso que "atrasa" o máximo possível um determinado processamento, fazendo-o somente quando for absolutamente
# necessário

def quadrado(x):
    return lambda: x * x


funcoes = [quadrado(i) for i in [1, 2, 3, 4, 5]]

print(funcoes)

for funcao in funcoes:
    print(funcao())
