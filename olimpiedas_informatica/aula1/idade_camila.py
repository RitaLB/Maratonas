"""
Idade de Camila

Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. 
Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.
Entrada

A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma das irmãs.
Saída

Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila. 
"""

# cibele > camila > celeste

idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

camila = 0

# Checando se camila é a idade 1
if ((idade1 >idade2) and (idade1 < idade3)) or ((idade1<idade2) and (idade1 > idade3)) :
    camila = idade1

#Checando idade 2
elif (idade2 > idade1) and (idade2 < idade3):
    camila = idade2
elif (idade2 < idade1) and (idade2 > idade3):
    camila = idade2

# Checando se camila é idade 3
else: 
    camila = idade3

print("A camila tem", camila, "anos")