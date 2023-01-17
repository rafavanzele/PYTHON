preco = float(input("Preco unitario do produto: R$"))
quant = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: R$"))

if preco * quant > dinheiro:
    faltam = preco * quant - dinheiro
    print(f"DINHEIRO INSUFICIENTE. FALTAM R${faltam:.2f}!")
else:
    troco = dinheiro - (quant * preco)
    print(f"TROCO: R${troco:.2f}")

