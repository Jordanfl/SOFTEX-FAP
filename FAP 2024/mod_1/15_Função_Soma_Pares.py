def soma_pares():
    num = int(input("Insira a quantidades de números: "))
    num_x = []
    for i in range(num):
        x = int(input(f"Insira o número: "))
        num_x.append(x)
    soma = 0
    for n in num_x:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos pares é: {soma}")

soma_pares()