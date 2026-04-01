salario = float(input("Informe seu salário: R$"))
tempo_de_serviço = int(input("Informe quantos anos presta serviços na empresa: ")) 
if tempo_de_serviço >= 6:
    bonus = salario * (5/ 100)
    aumento = salario + bonus
    print(f"Seu bônus é de R${bonus}")
    print(f"Seu sálario atual foi atualizado para R${aumento:.2f}!")
else:
    print("Funcionário não elegível para bônus.")
