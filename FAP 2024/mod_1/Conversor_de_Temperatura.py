def Celsius_fahrenheit(celsius):
  return celsius * 9/5 + 32

def fahrenheit_Celsius(fahrenheit):
  return (fahrenheit-32) * 5/9

escolha = input("Digite C para calcular a temperatura em Celsius e F para a temperatura em Fahrenheit: ").upper()

temperatura = float(input("Digite a temperatura desejada: "))

if escolha == "C":
  resultado_a = Celsius_fahrenheit(temperatura)
  print(f"{temperatura:.2f}°C é igual a {resultado_a:.2f}°F")

elif escolha == "F":  
  resultado_b = fahrenheit_Celsius(temperatura)
  print(f"{temperatura:.2f}°F é igual a {resultado_b:.2f}°C")
else:
  print("Por favor, digite 'C' ou 'F' para escolher a conversão. Tente novamente")


