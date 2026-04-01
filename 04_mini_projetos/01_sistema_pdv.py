produto = input("Nome do produto: ")
preco = float(input("Preço unitário (ex: 9.90): "))
qtd = int(input("Quantidade: "))

if preco <= 0 or qtd <= 0:
    print("Erro: preço e quantidade devem ser maiores que zero.")
else:
    subtotal = preco * qtd

if subtotal >= 100:
    if subtotal >= 200:
        desconto = subtotal *0.15
    else:
        desconto = subtotal *0.10
else:
    desconto = 0.0

total = subtotal - desconto

print("\n === RESUMO ===")
print("Produto", produto)
print("Subtotal: R$", subtotal)
print("Desconto R$", desconto)
print("Total:" ,total)
print("==============")
