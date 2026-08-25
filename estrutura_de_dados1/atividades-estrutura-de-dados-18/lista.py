numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("\nNúmeros digitados:")
for numero in numeros:
    print(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1

print("\nResultados:")
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade de números pares:", pares)
