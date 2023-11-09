# Geradores em python

# Os generator são iterators. MAS nem todos os iterators são um generator
# generators podem ser criados com funções geradoras (yield)
# generators podem ser criados com expressões geradoras

# Exemplo de função geradora

def contador(max):
    cont = 1
    while cont <= max:
        yield cont  # Retorna um valor e fica esperando a execução do método next(), se for executado o código continua
        cont += 1  # Esse comando yield só retorna um valor quando o método next() é executado, no fim gera um generator


gen = contador(5)
print(type(gen))
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen_2 = list(contador(10))
print(gen_2)


# função geradora com mais de um yield

def notas_musicais():
    yield 'Dó'
    yield 'Ré'
    yield 'Mi'
    yield 'Fa'
    yield 'Sol'
    yield 'Lá'
    yield 'Si'


gen_notas = notas_musicais()

for notas in gen_notas:
    print(notas)
