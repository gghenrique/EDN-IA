#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

try:
    n1 = float(input("Primeiro valor: "))
    op = input("Operação (+,-,*,/): ")
    n2 = float(input("Segundo valor: "))

    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    elif op == "/":
        resultado = n1 / n2
    else:
        print("Operação inválida.")
    print("Resultado:", resultado)

except ValueError:
    print("Valor inválido")
except ZeroDivisionError:
    print("Divisão por 0 não é permitido.")


