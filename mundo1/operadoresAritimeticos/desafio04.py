'''
Faca um programa que leia algo pelo taclado e mostre informacao sobre este tipo primitivo e todas
as informacoes possiveis sobre ele
'''
import json

algo = input("Informe alguma coisa: ")

print(type(algo))
print(algo.isalnum())
print(algo.isdecimal())


