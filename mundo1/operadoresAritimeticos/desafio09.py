'''
Crie um programa que leia um numero qualquer e mostre sua tabuada
'''

n = int(input("Informe um numero: "))

for cont in range (11):
    print(f"{cont} x {n} = {cont*n}")


