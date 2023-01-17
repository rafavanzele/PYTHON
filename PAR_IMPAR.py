N = int(input("Quantos numeros voce vai digitar? "))

for i in range(N):
    x = int(input("Digite um numero: "))
    if x == 0:
        print("NULO")
    else:
        if x % 2 == 0:
            print("PAR", end="")
        else:
            print("IMPAR", end="")
        if x > 0:
            print(" POSITIVO")
        else:
            print(" NEGATIVO")