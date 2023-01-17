m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

mat = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    print(f"Digite os elementos da {i + 1}a linha:")
    for j in range(n):
        mat[i][j] = float(input())


vet = [0 for x in range(m)]
for i in range(m):
    somalinha = 0
    for j in range(n):
        somalinha = somalinha + mat[i][j]
    vet[i] = somalinha


print("VETOR GERADO:")
for i in range(m):
    print(vet[i])