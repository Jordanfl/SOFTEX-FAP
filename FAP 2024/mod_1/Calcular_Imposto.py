salario = float(input("insira o seu salario: "))
def calcular_imposto(salario):
    if salario <= 2259.20:
        return 0
    elif salario >= 2259.21 and salario <= 2826.65:
        return (salario * 0.075) - 169.44
    elif salario >= 2826.66 and salario <= 3751.05:
        return (salario * 0.15) - 381.44
    elif salario >= 3751.06 and salario <= 4664.68:
        return (salario * 0.225) - 662.77
    else:
        return (salario * 0.275) - 896.00

imposto = calcular_imposto(salario)

print(f" Valor do Imposto é: R$ {salario} - R${imposto} = R${salario - imposto}")

