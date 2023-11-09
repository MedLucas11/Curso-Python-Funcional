# Implementando a função loop()

def loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it), end='')
        except StopIteration:
            break


nome = 'pyPRO'
lista = [1, 2, 3, 4, 5, 6, 7]

loop(nome)
print('')
loop(lista)
