# Verificando a memória com geradores
from sys import getsizeof


def fibonacci_lista(final):
    n1 = 0
    n2 = 1
    i = 2
    f = [n1, n2]

    if final == 1:
        return f[:1]

    elif final == 2:
        return f[:2]

    else:
        while i <= final:
            fibo = n1 + n2
            f.append(fibo)
            n1 = n2
            n2 = fibo
            i += 1
    return f


def fibonacci_gerador(final):
    fib1, fib2, limite = 0, 1, 0
    yield fib1
    while limite < final:
        fib1, fib2 = fib2, fib1 + fib2  # Precisa fazer em linha para os valores permanecerem corretos
        yield fib1
        limite += 1


gerador = fibonacci_gerador(10000)
lista = fibonacci_lista(10000)

print(f'Consumo de memória da lista: {getsizeof(lista)} bytes')
print(f'Consumo de memória do gerador: {getsizeof(gerador)} bytes')
