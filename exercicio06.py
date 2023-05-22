'''
    Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma nota menor que zero). 
    Após a entrada de dados, exiba:
    a. A quantidade de notas que foram informadas.
    b. Todas as notas na ordem em que foram informadas.
    c. A média aritmética de todas as notas. 
    d. A quantidade de notas acima da média aritmética calculada
'''

notas = []

while True:
    nota = float(input("Informe a nota do aluno: "))
    if nota < 0:
        print("Encerrando...")
        break
    else:
        notas.append(nota)

quantidadeNotas = len(notas)
mediaAritmetica = sum(notas) / quantidadeNotas
notasAcimaMedia = len([nota for nota in notas if nota > mediaAritmetica])

print(f"A quantidade de notas inseridas foram de {quantidadeNotas}")
print(f"As notas informadas foram: {notas}")
print(f"A média aritmética das notas é de {mediaAritmetica:.2f}")
print(f"As notas acimas da média aritmética de todas as notas foram {notasAcimaMedia}")
