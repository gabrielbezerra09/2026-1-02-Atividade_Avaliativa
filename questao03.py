soma = 0
numero = int(input("Digite um número."))
for i in range(1, numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print("O número é perfeito")
else:
    print("O número não é perfeito")