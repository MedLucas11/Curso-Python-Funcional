# O que são decoradores?

# Decoradores são funções, que "envolvem" outras funções e aprimoram seus comportamentos
# Decoradores tem uma sintaxe própria usando @

# Forma sem o syntax sugar (@)
def seja_educado(funcao):
    def sendo_educado():
        print('Olá...')
        funcao()
        print("Foi um prazer conhecê-lo(a)!")
    return sendo_educado


@seja_educado
def saudacao():
    print('Seja bem-vindo(a) ao projeto pyPRO!')


'''seja_educado(saudacao)'''

saudacao()
