# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100
valor_dolar = valor_reais * 5.2
valor_euro = valor_reais * 6.15

print(f"Para R$ {valor_reais:.2f}:\nDólares: $ {valor_dolar:.2f}\nEuros: € {valor_euro:.2f}")
