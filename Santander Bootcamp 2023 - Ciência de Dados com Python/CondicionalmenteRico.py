# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# Verificar se o saldo é suficiente para o saque
if saldo_total >= valor_saque:
    # Realizar o saque
    saldo_total -= valor_saque
    print("Saque realizado com sucesso. Novo saldo: {}".format(saldo_total))
else:
    # Informar que o saque não pode ser realizado
    print("Saldo insuficiente. Saque nao realizado!")