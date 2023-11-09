# Decoradores com parâmetros

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def original(*args):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento tem que ser {valor}'
            return funcao(*args)
        return original
    return interna


@verifica_primeiro_argumento(20)  # Podemos criar um decorador que verifica alguma condição
def calcula(num1, num2):
    return num1 + num2


print(calcula(20, 45))
print(calcula(10, 45))
