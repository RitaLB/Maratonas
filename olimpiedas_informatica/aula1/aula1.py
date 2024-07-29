# esse é um comentário olha só
"""
oioiii
esse é um comentário de mais de uma linha
outra linha
"""

#Variáveis:

nome_irma_1 = "Rita" # Isso é uma string
nome_irma_2 = "laura"

idade_irm1 = 8 # Isso é um inteiro, núme sem número
idade_irm2 = 10

#Float
preco_sorvete = 8.6 #Float: Número com vérgula

# dados de uma compra:
nome, idade, preco = "Rita", 18, 9.90

# Operadores
# =não significa "igual", significa atribuiição

# Operadores aritméticos

# + -> soma
bananas = 3 + 4
bananas = 9
# - -> subtração
abacaxis = bananas - 1

# * -> mutiplicação 
peixes = abacaxis * 3

# / -> divisão
iogurt = peixes / bananas

print("iogurt = ", iogurt)

# % -> módulo -> Resto da divisão inteira do operando da esquerda pelo da direita
i = 8 % 9
print("i =", i)
j = 9 % 8
print("j = ", j)
k = 13 % 6
print("k =", k)
l = 15 % 6
print("l=", l)

# // -> Divisão inteira: arredonda para baixo
div = 5 // 2
div2 = 3.5 // 2
print(div)
print(div2)

# ** -> expoente, potenciacao
pot1 = 2**3
print("pot 1 =", pot1)

# Operadores atribuição:
beijo = 2

beijo = beijo +2 
beijo += 2
flor = 5
flor = flor - 2
flor -= 1

# Operadores de comparação
# > -> maiort que
x = 7
y = 9
z = 1
print("x > z", x> z)

# < -> menor que
print ("x < x?", x < z)

# == -> igual
print( "x igual a z?", x == z)

# != -> diferente
print(" x diferente de z?" , x != z)

# >= -> mior igual
print("x >= z", x >= z)

# <= -> menor igual
print("x menor igual que z?", x <= z)

# Operadores lógicos: 
x = 1
y = 2
z = 3
w =100
# 0 para false e 1 para True

# and:
"""
A B |S
0 0 |0
0 1 |0
1 1 |1
"""
resposta =  (x > 2) and (z > x)
print("resposta = ", resposta)
resposta2 = ( x< 2) and (x == 1) and (z > y)
print("resposta 2 =", resposta2)

# or : PELO MENOS 1 afirmação (termo) tem que ser verdadeiro
resposta3 = (x == 1) or (x > 8) # True
resposta4 = (( x< 2) and (x == 1) and (z > y)) or (x == 100) # True

# not -> muda o valor
resposta6 = (x == 1) or (x > 8) # True
resposta7 = not(resposta6) # False
reposta8 = not(resposta7) # True


