livro = {}

livro["titulo"] = input("Digite o título: ")
livro["autor"] = input("Digite o autor: ")
livro["ano"] = int(input("Digite o ano: "))
livro["preco"] = float(input("Digite o preço: "))

print("\nDados do livro:")

for chave, valor in livro.items():
    print(f"{chave}: {valor}")

novo_preco = float(input("\nDigite o novo preço: "))
livro["preco"] = novo_preco

categoria = input("Digite a categoria do livro: ")
livro["categoria"] = categoria

print("\nDados atualizados:")

for chave, valor in livro.items():
    print(f"{chave}: {valor}")
