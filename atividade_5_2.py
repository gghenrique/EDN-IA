# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.


palavra = input("Digite a palavra: ")

if palavra == palavra[::-1]:
    print("Sim")
else:
    print("Não")
