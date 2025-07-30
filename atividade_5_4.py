#4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.


from datetime import datetime

# Entrada da data de nascimento (formato: dia/mês/ano)
nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string para data
data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

# Data atual
hoje = datetime.today()

# Calcula a diferença em dias
dias_vivo = (hoje - data_nascimento).days

# Mostra o resultado
print(f"Você está vivo há {dias_vivo} dias.")
