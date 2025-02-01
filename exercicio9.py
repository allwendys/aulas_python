altura = float(input("Qual sua altura?: "))
peso = float(input("Qual seu peso?: "))

imc = peso / (altura**2)
print("Seu imc é: ", imc)

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Você está no peso ideal")
elif imc >= 25 and imc <= 30:
    print("Você está no sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Você é obeso")
elif imc > 40:
    print("Você tem obesidade mórbida")
else:
    print("Inválido")