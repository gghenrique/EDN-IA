# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.

senha = input("Digite sua senha: ")
tamanho = len(senha)
numeros = 0

if tamanho >= 8:
    print(f"Sua senha possui {tamanho} caracteres. Aprovada no teste A.")
else:
    print(f"Sua senha possui {tamanho} caracteres. Reprovada no teste A.")

for i in senha:
    if i.isdigit():
        numeros += 1

if numeros >= 1:
    print(f"Sua senha possui {numeros} valores numéricos. Aprovada no teste B.")
else:
    print(f"Sua senha possui {numeros} valores numéricos. Reprovada no teste B.")
