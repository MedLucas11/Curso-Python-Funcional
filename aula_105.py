# Funções de Primeira Classe

# Capacidade de usar as funções como entidades de primeira classe (são tratadas como dados)
# As funções podem ser armazenadas em variáveis, por exemplo:

def dobro(x):
    return x*2


a = dobro

print(a(10))
