preco = float(input("Preco unitario do produto: "))
quant = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: R$"))

troco = dinheiro - (quant * preco)

print(f"TROCO: R${troco:.2f}")