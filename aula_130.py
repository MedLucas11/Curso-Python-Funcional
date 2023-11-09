# Decoradores pré-definidos

# A linguagem python já possui diversos decoradores definidos

# Exemplo, vamos modelar uma classe Casa

class Casa:
    def __init__(self, preco):
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco


minha_casa = Casa(450_000)
print(minha_casa.get_preco())

minha_casa.set_preco(500_000)
print(minha_casa.preco)


# Com o decorador @property você pode adicionar getters e setters "internamente" sem afetar a sintaxe usada para acessar
# ou modificar um atributo quando ele era público

class Casa2:
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0 and isinstance(novo_preco, float):
            self.__preco = novo_preco
        else:
            print('Insira um valor válido!')

    @preco.deleter
    def preco(self):
        del self.__preco


minha_casa2 = Casa2(450_000)
print(minha_casa2.preco)

minha_casa2.preco = 500_000.0
print(minha_casa2.preco)
# Posso acessar e modificar as informações mesmos ela sendo privada, graças ao @property
