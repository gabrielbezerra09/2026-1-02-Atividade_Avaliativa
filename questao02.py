import random

repeticoes = int(input("Digite quantas vezes voce quer um numero aleatorio."))

for i in range(1, repeticoes + 1):
    print(i, "numero aleatorio:", random.randint(1,100))