glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100.0:
    print("Classificacao: NORMAL")
elif glicose <= 140.0:
    print("Classificacao: ELEVADO")
else:
    print("Classificacao: DIABETES")