N = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(N)]

for i in range(N):
    vet[i] = float(input("Digite um numero: "))


maiorvalor = vet[0]
posmaior = 0
for i in range(N):
    if vet[i] > maiorvalor:
        maiorvalor = vet[i]
        posmaior = i

print(f"MAIOR VALOR: {maiorvalor}")
print(f"POSICAO DO MAIOR VALOR: {posmaior}")
