# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"


try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura*altura)
    if imc < 18.5:
        print(f"Seu IMC é: {imc:.2f}\nSua classificação é: Abaixo do peso.")
    elif imc < 25:
        print(f"Seu IMC é: {imc:.2f}\nSua classificação é: Peso Normal.")
    elif imc < 30:
        print(f"Seu IMC é: {imc:.2f}\nSua classificação é: Sobrepeso.")
    else:
        print(f"Seu IMC é: {imc:.2f}\nSua classificação é: Obeso.")

except ValueError:
    print("Valor inválido")
except ZeroDivisionError:
    print("Divisão por 0 não é permitido.")



