'''
Faca um programa que leia a altura e largura de uma parede em metros,
calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta,
pinta uma area de 2m²
'''

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))

area = altura * largura

tinta = area/4

print(f"A area da parede é: {area}")
print(f"A quantidade de tinta em litros é: {tinta}")

