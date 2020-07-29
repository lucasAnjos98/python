'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
mostre o comprimento da hipotenusa.
'''

import math

catO = float(input("Informe o cateto oposto: "))
catA = float(input("Informe o cateto adjacente: "))

hypot = math.hypot(catO, catA)

print(f"A hipotenuza é: {hypot:.2f}")
