# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

produto = "Camiseta"
preço_original = 50
desconto = 0.20
valor_desconto = preço_original - preço_original*desconto
print("================= Nota Fiscal =================")
print(f"Produto: {produto}\nPreço original: R$ {preço_original:.2f}\nDesconto Aplicado: {desconto*100:.2f} %")
print("------------------------------------------------")
print(f"Total: R$ {valor_desconto:.2f}")
print("------------------------------------------------")