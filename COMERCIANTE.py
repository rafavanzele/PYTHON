N = int(input("Serao digitados quantos produtos? "))

produto = [0 for x in range(N)]
compra = [0 for x in range(N)]
venda = [0 for x in range(N)]
porcLucro = [0 for x in range(N)]

for i in range(N):
    print(f"Produto {i+1}")
    produto[i] = str(input("Nome: "))
    compra[i] = float(input("Preco de compra: R$ "))
    venda[i] = float(input("Preco de venda: R$ "))

for i in range(N):
    porcLucro[i] = (venda[i] - compra[i]) / compra[i] * 100.0

abaixo = 0
entre = 0
acima = 0
for i in range(N):
    if porcLucro[i] < 10.0:
        abaixo = abaixo + 1
    elif porcLucro[i] < 20.0:
        entre = entre + 1
    else:
        acima = acima + 1

totalcompra = 0
totalvenda = 0
for i in range(N):
    totalcompra = totalcompra + compra[i]
    totalvenda = totalvenda + venda[i]

lucroTotal = totalvenda - totalcompra

print()
print("RELATORIO FINAL")
print(f"Lucro Abaixo de 10%: {abaixo}")
print(f"Lucro Entre 10% e 20%: {entre}")
print(f"Lucro Acima de 20%: {acima}")
print(f"Valor total de compra: R${totalcompra:.2f}")
print(f"Valor total de venda: R${totalvenda:.2f}")
print(f"Lucro Total: R${lucroTotal:.2f}")
