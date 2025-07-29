# 4 - Criar um código que serve para analisar números digitados pelo usuário,
# classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

pares = 0
impares = 0

while True:
    try:
        n = int(input("Número: "))
        if n%2 == 0:
            pares += 1
            print(f"o número {n} é par.")
        else:
            impares += 1
            print(f"o número {n} é impar.")
    except ValueError:
        print("Valor inválido. Leituras encerradas.")
        break

print(f"Você digitou {pares} números pares e {impares} números impares.")
