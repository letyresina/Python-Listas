'''
    Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e os 
    números ímpares em outra lista. Exiba as duas listas ao usuário.
'''

numeros = []
pares = []
impares = []

for i in range(10):
    num = int(input("Informe um número inteiro qualquer: "))
    numeros.append(num)

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(f"\n Os números pares são {pares} \n Os ímpares são {impares}")