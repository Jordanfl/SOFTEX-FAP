import math

def calc():
    C = float(input("Comprimento do depósito (cm): "))
    L = float(input("Largura do depósito (cm): "))
    A = float(input("Altura do depósito (cm): "))
    bola = input("Insira o tipo de bola(futebol,basquete e etc..): ").lower()
    
    bolas = {
        "futebol": 22,
        "basquete": 24,
        "basquete infantil": 22,
        "volei": 21,
        "vôlei": 21,
        "handball": 19,
        "handebol": 19,
        "futsal": 20,
        "futebol de salão": 20
    }
    
    diametro = bolas.get(bola)
    
    if diametro is None:
        diametro = float(input("Erro, insira manualmente o diâmetro da bola (cm): "))
        
    raio = diametro / 2
    volumedep = C * L * A
    ballvol = (4/3) * math.pi * (raio ** 3)
    resultado = volumedep // ballvol
    
    print(f"O número aproximado de bolas que cabem no depósito é: {resultado}")

calc()
