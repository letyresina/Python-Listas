'''
    Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba: 
    a. A média aritmética dos números armazenados na lista.
    b. O somatório dos números pares armazenados na lista.
'''

numeros = []


for i in range(10):
    num = int(input("Informe um número inteiro qualquer: "))
    numeros.append(num)

i = 0
for item in numeros:
    if item % 2 == 0 :
        i += 1

mediaAritmetica = sum(numeros) / 10

print(f"A quantidadede números pares é de {i} e a média artmética é {mediaAritmetica}")