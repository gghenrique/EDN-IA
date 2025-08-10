# 1 - Crie um programa que gera uma senha aleatória com o módulo
# random, utilizando caracteres especiais, possibilitando o
# usuário a informar a quantidade de caracteres dessa senha
# aleatória.


import random


tamanho = int(input("Digite o tamanho da senha: "))

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()"

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)


print("Senha gerada: ", senha)
