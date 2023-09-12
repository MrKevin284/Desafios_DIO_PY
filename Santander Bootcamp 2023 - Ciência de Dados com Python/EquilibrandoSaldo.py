saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

# Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

# Imprimir a saída conforme a tabela de exemplos (uma casa decimal).
print("Saldo atualizado na conta: {:.1f}".format(saldo_atualizado))
