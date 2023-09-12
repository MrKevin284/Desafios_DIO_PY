valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# Iterar, baseado no período em anos, para cálculo do valorFinal com os juros.
for _ in range(periodo):
    valor_final *= (1 + taxa_juros)

# Arredondar para duas casas decimais
valor_final = round(valor_final, 2)

print("Valor final do investimento: R$", valor_final)
