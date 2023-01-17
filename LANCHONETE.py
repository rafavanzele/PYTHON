codigo = int(input("Codigo do produto comprado: "))
quant = int(input("Quantidade comprada: "))

if codigo == 1:
    valor = quant * 5.0
elif codigo == 2:
    valor = quant * 3.50
elif codigo == 3:
    valor = quant * 4.80
elif codigo == 4:
    valor = quant * 8.90
elif codigo == 5:
    valor = quant * 7.32

print(f"VALOR A PAGAR: R${valor:.2f}")
