mllata = (350)
mlgarrafaM = (600)
mlgarrafaG = (2000)

lata = int(input("Quantas latas você quer comprar?: "))
garrafaM = int(input("Quantas garrafaM você quer comprar?: "))
garrafaG = int(input("Quantas garrafaG você quer comprar?: "))

print ("Você está comprando" , (lata * mllata + garrafaM * mlgarrafaM+ garrafaG * mlgarrafaG) , "ml de refrigerante")
  
rml = (lata * mllata + garrafaM * mlgarrafaM+ garrafaG * mlgarrafaG) / 1000

print("Ou" , rml ,"litros de refrigerante")