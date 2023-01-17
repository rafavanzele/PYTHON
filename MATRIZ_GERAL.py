import math

N = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

print()
soma = 0
print("SOMA DOS POSITIVOS:", end="")
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print(f" {soma:.1f}")



print()
indlinha = int(input("Escolha uma linha: "))
print("Linha escolhida: ", end="")

for i in range(N):
    print(f"{mat[indlinha][i]:.1f} ", end=" ")


print()
indlinha = int(input("Escolha uma coluna: "))
print("Coluna escolhida: ", end="")

for i in range(N):
    print(f"{mat[i][indlinha]:.1f} ", end="")


print()
print("Diagonal Principal: ", end=" ")
for i in range(N):
    print(f" {mat[i][i]:.1f} ", end="")


print()
for i in range(N):
    for j in range(N):
        if mat[i][j] < 0:
            mat[i][j] = math.pow(mat[i][j], 2)


print("MATRIZ ALTERADA:")
for i in range(N):
    for j in range(N):
        print(f"{mat[i][j]:.1f} ", end=" ")
    print()
