haf = float(input("Quantas horas de atividade física você fez no mês?: "))

if haf == 10:
    h1=(haf*2)
    print(f"Você ganhará {(h1*0.05)} reais")
elif haf >=10 and haf <=20:
    h2=(haf*5)
    print(f"Você ganhará {(h2*0.05)} reais")
elif haf >20:
    h3=(haf*10)
    print(f"Você ganhará {(h3*0.05)} reais")
else:
    print("Inválido")