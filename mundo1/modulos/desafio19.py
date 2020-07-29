'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
dos alunos e escrevendo na tela o nome do escolhido.
'''

import random

alunos = [input(f"Informe o nome do aluno: "), input(f"Informe o nome do aluno: "), input(f"Informe o nome do aluno: "), input(f"Informe o nome do aluno: ")]
n = random.randrange(0, 4)

print(f"O aluno escolhido foi: {alunos[n]}")