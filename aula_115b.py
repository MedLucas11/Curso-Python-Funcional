# Utilizando list comprehension e zip()

# Imagine que queremos identificar a maior venda de cada produto, dados duas listas de vendas

venda1 = [1200, 234, 2345, 1560]
venda2 = [1245, 300, 2103, 1434]
produtos = ['fogão', 'liquidificador', 'geladeira', 'tv']

lista_maiores_vendas = {venda[0]: max(venda[1], venda[2]) for venda in zip(produtos, venda1, venda2)}
print(lista_maiores_vendas)
