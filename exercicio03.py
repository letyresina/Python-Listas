'''
    Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba: 
    a. a lista com todos os itens armazenados. 
    b. o somatório de todos os números contidos na lista. 
    c. o maior número da lista. 
    d. o menor número da lista.
'''
import random 

numeros = []

for i in range(20):
    numeros.append(random.randint(1,20))

print(f"Os números sorteados foram: {numeros}")
print(f"A somatória de todos os números são {sum(numeros)}")
print(f"O maior número da lista é {max(numeros)}")
print(f"O menor número da lista é {min(numeros)}")