N = int(input("Deseja tabuada para qual numero? "))

for i in range(0, 11):
    produto = i * N
    print(f"{N} x {i} = {produto}")