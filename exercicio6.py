m1 = float(input("Qual a média do 1° trimestre? "))
m2 = float(input("Qual a média do 2° trimestre? "))
m3 = float(input("Qual a média do 3° trimestre? "))
m4 = float(input("Qual a média do 4° trimestre? "))

s4 = (m1 + m2 + m3 + m4)
mf = (s4/4)

print("Sua média anual é " , mf)

if mf >=7 and mf <=10:
    print("Você está aprovado!")
elif mf >=5 and mf < 7:
    print("Você está de recuperação!")
elif mf >=0 and mf < 5:
    print("Você está reprovado!")
else:
    print("Média inválida.")