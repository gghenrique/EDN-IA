# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado:.2f}°F")

elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
    print(f"{temperatura}°C = {resultado:.2f}K")

elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado:.2f}°C")

elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura}°F = {resultado:.2f}K")

elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
    print(f"{temperatura}K = {resultado:.2f}°C")

elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura}K = {resultado:.2f}°F")

elif origem == destino:
    print(f"A temperatura já está em {destino}: {temperatura}")

else:
    print("Unidade inválida. Use C, F ou K.")
