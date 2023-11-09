# Recursividade

# Propriedade de uma função chamar a si mesma
# Necessariamente, toda função recursiva dever ter uma ou mais condições de parada

"""def fatorial(n):
    if n > 1:
        return n * fatorial(n-1)
    else:
        return 1"""


def fatorial(n):
    return (n * fatorial(n - 1)) if n > 1 else 1


print(fatorial(5))
