contador = 0

perguntas = [
"Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?",
]

for i in perguntas:
    resposta = input(i + "sim/não): ").lower()
    if resposta == "sim":
        contador += 1 

if contador == 0 or contador == 1:
    print("Inocente")

elif contador == 2: 
    print("Suspeito")

elif contador == 3 or contador == 4: 
    print("Cúmplice")

elif contador == 5: 
    print("Assasino")

