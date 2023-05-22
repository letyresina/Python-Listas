'''
    Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as idades em 
    outra lista. Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou 
    igual a 18 anos.
'''

nomes = []
idades = []

def buscarIdade(nomes, idades):
    for i in range(len(nomes)):
        if idades[i] >= 18:
            print(f"As pessoas com 18 anos ou mais são: {nomes[i]}")


for i in range(10):
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    nomes.append(nome)
    idades.append(idade)

buscarIdade(nomes, idades)
