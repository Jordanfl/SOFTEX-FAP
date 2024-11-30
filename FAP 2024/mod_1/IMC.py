while True:
  altura = float(input("Insira sua altura em metros: "))
  peso = float(input("Insira seu peso em kg:  "))

  if peso >= 15 and peso <= 250 and altura >= 0.6 and altura <= 2.5:
      imc = peso / (altura ** 2)

      if imc < 18.5:
          resultado = "Abaixo do peso"
      elif imc >= 18.5 and imc <= 24.9:
          resultado = "Peso normal"
      elif imc >= 25.0 and imc <= 29.9 :
          resultado = "Sobrepeso"
      elif imc >= 30.0 and imc <= 34.9:
          resultado = "Obesidade grau I"
      elif imc >= 35.0 and imc <= 39.9:
          resultado = "Obesidade grau II"
      else:
          resultado = "Obesidade grau III"

      print(f"IMC: {imc:.2f}")
      print(f"Resultado: {resultado}")
      break  
  else:
      print("Dados inválido. Tente novamente.")