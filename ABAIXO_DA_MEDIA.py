N = int(input("Quantos elementos vai ter o vetor? "))

vet = [0 for x in range(N)]

for i in range(N):
    vet[i] = float(input("Digite um numero: "))

soma = 0
for i in range(N):
    soma = soma + vet[i]

media = (float(soma)) / N

print(f"MEDIA DO VETOR: {media:.3f}")

print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(N):
    if vet[i] < media:
        print(vet[i])
