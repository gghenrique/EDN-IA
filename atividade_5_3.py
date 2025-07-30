# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

# Função para calcular o valor com desconto
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    final = preco - desconto
    return round(final, 2)  # arredonda para 2 casas decimais

# Interação com o usuário
preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto (%): "))

# Calcula e mostra o resultado
preco_final = calcular_desconto(preco, percentual)
print(f"Preço final com desconto: R$ {preco_final}")
