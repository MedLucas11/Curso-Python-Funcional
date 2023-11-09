# Função zip()

# Essa função constrói uma série de sequências a partir de outra série de sequências, de forma que os elementos da
# primeira sequência gerada são os primeiros elementos de todas as sequências originais e assim por diante

print(list(zip([1, 3, 5], [2, 4, 6])))  # O zip() retorna um objeto assim como o map() e o filter()

print(list(zip([1, 3, 5], [2, 4, 6, 8, 10])))  # Nesse caso ele ignora os elementos "a mais"


# Podemos misturar diferentes tipos de iteráveis na função zip, diferentes estruturas de dados

tupla = (1, 2, 3, 4, 5, 6, 7)
lista = [11, 12, 13, 14, 15, 16, 17]
dicionario = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25}

zp = zip(tupla, lista, dicionario.values())
print(list(zp))
