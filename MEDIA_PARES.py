n = int(input("Quantos elementos vai ter o vetor? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um numero: "))

soma = 0
qtdpares = 0

for i in range(n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        qtdpares = qtdpares + 1

if qtdpares == 0:
    print("NENHUM NUMERO PAR")

else:
    media = (float(soma)) / qtdpares

print(f"MEDIA DOS PARES: {media:.2f}")

