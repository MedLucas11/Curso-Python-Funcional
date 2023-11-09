# Decoradores com diferentes assinaturas

# A assinatura de uma função nada mais é que o seu NOME, seus PARÂMETROS DE ENTRADA e o seu RETORNO

def falar_alto(funcao):
    def maiscula(*args):
        return funcao(*args).upper()
    return maiscula


@falar_alto
def saudacao(palavra):
    return f'Olá! {palavra}'


@falar_alto
def pedido(bola1, bola2):
    return f'Olá quero sorvete de {bola1} e {bola2}'


print(saudacao('Bom Dia!'))
print(pedido('morango', 'chocolate'))
