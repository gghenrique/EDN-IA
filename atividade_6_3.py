# 3 - Desenvolva um programa que consulte informações de
# endereço a partir de um CEP fornecido pelo usuário, utilizando
# a API ViaCEP. O programa deve exibir o logradouro, bairro,
# cidade e estado correspondentes ao CEP consultado.


import requests


cep = input("Digite o CEP (somente números): ")

resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

dados = resposta.json()

print("Logradouro: ", dados["logradouro"])
print("Bairro: ", dados["bairro"])
print("Cidade: ", dados["localidade"])
print("Estado: ", dados["uf"])
