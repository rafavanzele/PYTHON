N = int(input("Quantos casos de teste serao digitados? "))

coelho = 0
sapo = 0
rato = 0
for i in range (N):
    x = int(input("Quantidade de cobaias: "))
    tipo = str(input("Tipo de cobaia: "))

    if tipo == 'C':
        coelho = coelho + x
    elif tipo == 'S':
        sapo = sapo + x
    else:
        rato = rato + x

total = coelho + sapo + rato
percCoelho = (coelho / total) * 100.0
percRato = (rato / total) * 100.0
percSapo = (sapo / total) * 100.0

print()
print("RELATORIO FINAL")
print(f"Total de cobaias: {total}")
print(f"Total de Coelhos: {coelho}")
print(f"Total de Ratos: {rato}")
print(f"Total de Sapos: {sapo}")
print(f"Percentual de Coelhos: {percCoelho:.2f}%")
print(f"Percentual de Ratos: {percRato:.2f}%")
print(f"Percentual de Sapos: {percSapo:.2f}%")