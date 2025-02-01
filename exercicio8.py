idd = int(input("Qual a sua idade?: "))

# if hv == 1 and idd > 18:
#     print("Você pode dirigir")
# elif hv == 2 and idd > 18:
#     print("Você não pode dirigir")
# elif hv == 2 and idd < 18:
#     print("Você não pode dirigir")
# else:
#     print("Inválido")
    
    
if idd >=18:
    have_cnh = input("Você já tem CNH? (s para sim e n para não): ")
    if have_cnh == "s":
    # if have_cnh.lower().startswith(s) == "s":
            print("Você pode dirigir.")
    elif have_cnh == "n":
            print("Você não pode dirigir")
    else:
            print("Inválido, digite s ou n")
else:
    print(f"Você não pode tirar a CNH, aguarde {(18-idd)} {"ano" if 18-idd == 1 else "anos"}")