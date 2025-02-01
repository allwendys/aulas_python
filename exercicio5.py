eachfqj = (50)
eachfps = (50)
eachfhb = (100)

#um sanduíche contem 2 eachfqj + 1 eachfps + 1 eachfhb

qntd = int(input("Quantos sanduíches você quer?: "))

# print("Será necessário de: ")
# print(2*eachfqj * qntd)
# print(eachfps * qntd)
# print(eachfhb * qntd)

print("Gramas de queijo: ", (2*eachfqj * qntd))
print("Gramas de presunto: ", (eachfps * qntd))
print("Gramas de presunto: ", (eachfhb * qntd))