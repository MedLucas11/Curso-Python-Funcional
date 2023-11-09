# Closure

# Capacidade da função perceber o "entorno". Tem consciência do local onde ela foi escrita. Além do escopo interno, ela
# percebe o que está ao seu redor

# Consiste em retornar uma função que internamente variáveis (ou nomes) da função que a define


def multiplicar(x):
    def calcular(y):
        return x*y
    return calcular


dobro = multiplicar(2)
triplo = multiplicar(3)

print(dobro)
print(triplo)

print(dobro(10))
print(triplo(10))
