#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

notas = 0
alunos = 0

while True:
    try:
        nota = float(input("Nota: "))
        notas += nota
        alunos += 1
    except ValueError:
        print("Valor invalído. Leitura de notas encerrada.")
        break

try:
    media = notas/alunos
    print(f"Média da turma com {alunos} alunos: {media:.2f}")
except ZeroDivisionError:
    print("Divisão por 0 não é permitida.")