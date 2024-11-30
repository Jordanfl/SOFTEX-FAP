número_1 = int(input("Insira um número: "))
número_2 = int(input("Insira um número: "))

if número_1 < número_2:
    for n in range(número_1,número_2 + 1):
        print(n)
else: 
     for n in range(número_1,número_2 -1,-1):
         print(n)