'''
Faca um programa que leia o preco de um produto e mostre seu novo preco com 5% de desconto
'''

precoProduto = float(input("Informe o preco do produto: "))

novoPreco = precoProduto - (precoProduto*0.05)

print(f"O novo preco do produto é: {novoPreco:.2f}")