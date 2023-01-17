N = int(input("Quantos numeros voce vai digitar? "))

dentro = 0
fora = 0
for i in range(0, N):
    x = int(input("Digite um numero: "))
    if x < 10 or x > 20:
        fora = fora + 1
    else:
        dentro = dentro + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")

