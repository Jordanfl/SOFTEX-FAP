import random

rand_n = random.randint(0,100)
tentativas = 0
print("Bem Vindo ao Jogo do Número Secreto")
print("Tente adivinhar o número secreto entre 0 e 100")
while True:
    n = int(input("Insira o seu número secreto: "))
    tentativas += 1 
    if 0 <= n <= 100:
        if rand_n > n:
           print("O número secreto é maior")
        elif rand_n < n:
           print("O número secreto é menor")
        else:
            print(f"Parabéns você descobriu o número secreto em {tentativas} tentativas")
            break

    else:
        print("Número inválido, insira o número secreto entre 0 e 100")

    