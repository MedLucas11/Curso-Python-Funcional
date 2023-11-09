# Função reversed()

# Essa função inverte qualquer iterável, não modificando o iterável original
# Diferente do método reverse() que funciona apenas em listas e alterando a lista original

lista = [1, 2, 3, 4, 5, 6, 7]

reverso = reversed(lista)
print(list(reverso))

# Mostrando uma string em forma reversa

frase = 'pyPRO - Seja um profissional Python!'

for letra in reversed(frase):
    print(letra, end='')  # O parâmetro end= indica onde fica o final do print, permitindo q seja impresso na msm linha
