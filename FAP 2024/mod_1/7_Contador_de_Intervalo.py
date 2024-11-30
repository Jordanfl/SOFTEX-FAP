num = int(input("Insira a quantidades de números: "))

intervalo_1 = []
intervalo_2 = []
intervalo_3 = []
intervalo_4 = []

for i in (range(num)):
    x = int(input(f"Insira o número: "))
     
    if x < 0:
       print("Tente novamente, Todos os números precisam ser positivos.")
       break
    if x >= 0 and x <= 25:
        intervalo_1.append(x)
    elif x >= 26 and x <=50:
        intervalo_2.append(x)
    elif x >= 51 and x <= 75:
        intervalo_3.append(x)
    elif x >= 76 and x <= 100:
        intervalo_4.append(x)
        
    print(f"intervalo 1 {intervalo_1}")
    print(f"intervalo 2 {intervalo_2}")
    print(f"intervalo 3 {intervalo_3}")
    print(f"intervalo 4 {intervalo_4}")