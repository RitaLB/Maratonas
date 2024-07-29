# -*- coding: utf-8 -*-
"""Dado qualquer inteiro n (1 ≤ n ≤ 10000) não divisível por 2 ou por 5, 
algum múltiplo de n deve ser um número que é uma sequência de números 1. 
Você deve então calcular e mostrar quantos dígitos tem o menor múltiplo de n 
tem todos seus dígitos iguais a 1."""
    
num_dig_1 = {}

for i in range (0,12):
    tudo_1 = True
    digitos = []
    stri = str(i)
    print(stri)
    for digito in range (len(stri)):
        digitos.append(stri[digito])
    print(digitos)
    for digito in digitos:
        if digito != "1": 
            tudo_1 = False
    if tudo_1 == True:
            numero_com_1 = int(i)
            num_dig_1[numero_com_1] = numero_com_1
    print("meu dicionario =", num_dig_1)


while True:
    try:
        numero = input()
        multiplicador = 3
        procurando_multiplo = True
        numero_antigo = numero
        while procurando_multiplo:
            numero_antigo = numero
            if numero in num_dig_1:
                menor_multiplo = numero
                procurando_multiplo = False
            else :
                numero = numero_antigo * multiplicador
    except EOFError:
        break
    
    