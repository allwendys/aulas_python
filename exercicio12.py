# for i in range(101):
#      print(i)
     
# for i in range (1, 101):
#     if i % 3==0 and i % 5==0:
#         print(i , " É múltiplo de 3 e de 5")
#     elif i % 3==0:
#         print(i , " É múltiplo de 3 ")
#     elif i % 5==0:
#         print(i , " É múltiplo de 5 ")
    
num = int(input("Digite um número: "))
fatorial = 1

for i in range(1, num +1):
    fatorial *= i
    
print(f"O fatorial de {num} é igual a {fatorial}")
