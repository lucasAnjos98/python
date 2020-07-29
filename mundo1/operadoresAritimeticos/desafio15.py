'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

qtdeKm = float(input("Informe a quantidade de Km percorridos pelo carro: "))

qtdeDias = int(input("Informe a quantidade de dias: "))

preco = (qtdeDias * 60) + (qtdeKm * 0.15)

print(f"O preco a se pagar é: R${preco:.2f}")

