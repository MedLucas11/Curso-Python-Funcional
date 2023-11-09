# Função map()

# Consiste em aplicar uma função a todos os itens de uma sequência, gerando outra lista contendo so resultados com o
# mesmo tamanho da lista inicial

# Estrutura básica: map('função' ou 'None", sequência) -> retorna uma lista

# Exemplos:

map(None, [1, 2, 3])  # None não vai aplicar função na lista

positivos = map(abs, [-1, -2, -3])  # A função map() retorna um OBJETO
print(list(positivos))  # Por isso é necessário atribuir e converter para a estrutura de dados que queremos

string = map(str, [1, 2, 3])
print(list(string))

hexadecimal = map(hex, [10, 11, 12])
print(list(hexadecimal))
print(list(hexadecimal))  # Quando fazemos uma transformação dessa forma nós "consumimos" o resultado da memória e
# ele some, resultando em uma lista vazia

# Se quisermos utilizar mais de uma vez, devemos fazer uma atribuição em uma variável e guardar o resultado:
hexadecimal_2 = map(hex, [10, 11, 12])
lista_hexadecimal = list(hexadecimal_2)
print(lista_hexadecimal)
print(lista_hexadecimal)

