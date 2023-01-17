N = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(N)]

for i in range(N):
    vet[i] = int(input("Digite um numero: "))

pares = 0
for i in range(N):
    if vet[i] % 2 == 0:
        pares = pares + 1

print("NUMEROS PARES:")
for i in range(N):
    if vet[i] % 2 == 0:
        print(vet[i], end=" ")

print()
print(f"QUANTIDADE DE PARES: {pares}")