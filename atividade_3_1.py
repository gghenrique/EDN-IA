# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

try:
    idade = int(input("Digite sua idade: "))
    
    if 0 <= idade <= 12:
        print(f"Sua idade é {idade}. Você é uma Criança.")
    if 13 <= idade <= 17:
        print(f"Sua idade é {idade}. Você é um(a) Adolescente.")
    if 18 <= idade <= 59:
        print(f"Sua idade é {idade}. Você é um Adulto.")
    if idade >= 60:
        print(f"Sua idade é {idade}. Você é um(a) idoso(a).")
    else: #Valores negativos
        print("Idade Invalída")

except ValueError:
    print("Valor inválido")