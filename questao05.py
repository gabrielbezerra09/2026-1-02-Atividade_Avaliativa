repeticoes = int(input("Digite quantos números inteiros positivos quer escrever:"))
contador = 0
numeros= []
for i in range(repeticoes):
    numeros.append(int(input()))

soma=sum(numeros)
media = soma / repeticoes
maior = max(numeros)
menor = min(numeros)
for numero in numeros:
    if numero > media:
        contador += 1

print(f"a soma total é {soma}")
print(f"a média é {media}")
print(f"o maior valor é {maior}")
print(f"o menor valor é {menor}")
print(f"a quantidade de numeros acima da média é {contador}")