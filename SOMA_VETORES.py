N = int(input("Quantos valores vai ter cada vetor? "))

A = [0 for x in range(N)]
B = [0 for x in range(N)]
C = [0 for x in range(N)]

print("Digite os valores do vetor A:")
for i in range(N):
    A[i] = int(input())


print("Digite os valores do vetor B:")
for i in range(N):
    B[i] = int(input())


for i in range(N):
    C[i] = A[i] + B[i]

print(f"VETOR RESULTANTE:")
for i in range(N):
    print(C[i])

