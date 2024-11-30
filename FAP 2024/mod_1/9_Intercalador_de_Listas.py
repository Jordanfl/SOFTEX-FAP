def intercalador_de_listas():
    lista1 = []
    lista2 = []
    print("Digite os dados da primeira lista:")
    for i in range(10):
        dado = int(input(f"dado {i+1}: "))
        lista1.append(dado)
    print("Digite os dados da segunda lista:")
    for i in range(10):
        dado = int(input(f"dado {i+1}: "))
        lista2.append(dado)
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada
lista_final = intercalador_de_listas()
print(lista_final)