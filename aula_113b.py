import statistics

# Utilizando a biblioteca statistics para calcular média de uma lista e filtrar elementos maiores que a média

dados = [1.2, 3, 3.4, 5, 2.4, 7.4, 5.9, 1.3, 0.4, 7.5]
media = statistics.mean(dados)
print(media)

acima_da_media = filter(lambda x: x > media, dados)
print(list(acima_da_media))
