cliente = input("Cliente: ")
produto = input("Produto: ")
vo = float(input("Valor: R$")) #valor original
desconto = 3.0
tp = vo-desconto #total pago
print("----- Recibo de Compra -----")
print(f"Cliente: {cliente}")
print(f"Produto:            {produto}")
print(f"Valor Original:     R${vo}")
print(f"Desconto :          R${desconto}")
print()
print(f"Total Pago:         R${tp}")
print("----------------------------")
