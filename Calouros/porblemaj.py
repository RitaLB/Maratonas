import math

nrodadas = int(input())
for i in range(nrodadas):
    dados = input().split()
    d1 = int(dados[0])
    d2 = int(dados[1])
    nradares = math.ceil(d1/d2)

    print(nradares)