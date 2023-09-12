valor = float(input())

if valor > 0:
    print("Deposito realizado com sucesso!")
    print("Saldo atual: R$ {:.2f}".format(valor))
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor invalido! Digite um valor maior que zero.")
