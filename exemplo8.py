gente = {"nome": "Raquel", "idade": 16, "cidade": "Manaus", "pode_dirigir": False}

#para manipular
for chave in gente:
    print(chave)
    
for valor in gente.values():
    print(valor)
    
for chave, valor in gente.items():
    print (f"Chave: {chave}, Valor: {valor}")

gente.update({"idade": 17, "cidade": "São Paulo"})
    

#para exibir    
print(gente.keys())
print(gente.values())
print(gente.items())