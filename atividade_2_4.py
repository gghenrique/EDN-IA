# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

distancia = 300
combustivel = 25

consumo = distancia/combustivel

print(f"Considerando uma viagem de distância de {distancia} Km e um consumo de {combustivel} L de combustível:\nMédia de Consumo = {consumo:.2f} Km/L")