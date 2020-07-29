'''
Faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
'''

salario = float(input("Informe seu salario: "))

novoSalario = salario + (salario*0.15)

print(f"O novo salario é: {novoSalario:.2f}")