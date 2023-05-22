'''
    Faça uma função que recebe como parâmetro uma lista e um número. A função deve retornar a quantidade de 
    vezes que o número aparece na lista. No programa principal, preencha a lista com 10 números aleatórios e 
    solicite um número ao usuário. Envie as informações para a função e exiba o seu retorno.
'''

import random 

def buscarNumero(lista, num):
    i = 0
    for item in lista:
        if item == num:
            i += 1
    return i

numerosAleatorios = []

for i in range(10):
    numerosAleatorios.append(random.randint(1,10))

#print(numerosAleatorios)

num = int(input("Informe um número qualquer: "))

quantidade = buscarNumero(numerosAleatorios, num)

if quantidade == 0:
    print("Não encontrou o número")
else:
    print(f"Esse número apareceu {quantidade} vezes")