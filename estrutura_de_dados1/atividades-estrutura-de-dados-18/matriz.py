matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

print("\nMatriz:")

for linha in matriz:
    print(*linha)

soma = 0
soma_diagonal = 0
maior = matriz[0][0]

for i in range(3):
    for j in range(3):
        soma += matriz[i][j]

        if i == j:
            soma_diagonal += matriz[i][j]

        if matriz[i][j] > maior:
            maior = matriz[i][j]

print("\nSoma de todos os elementos:", soma)
print("Soma da diagonal principal:", soma_diagonal)
print("Maior elemento:", maior)
