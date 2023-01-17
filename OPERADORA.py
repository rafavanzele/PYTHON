minutos = int(input("Digite a quantidade de minutos: "))

if minutos <= 100:
    print("VALOR A PAGAR: R$ 50.00")
else:
    valor = 50.00 + ((minutos - 100) * 2)
    print(f"VALOR A PAGAR: {valor:.2f}")

