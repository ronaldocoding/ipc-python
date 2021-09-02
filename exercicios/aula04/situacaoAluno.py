"""
Escreva uma expressão que decida se um aluno foi ou não aprovado. Para ser aprovado, todas as notas do aluno devem ser
maiores ou iguais a 7,0. Considere que o aluno realizou três avaliações
"""

nota1 = float(input('Nota 1: ')) #Recebe nota1 do usuário
nota2 = float(input('Nota 2: ')) #Recebe nota2 do usuário
nota3 = float(input('Nota 3: ')) ##Recebe nota3 do usuário

situacao = ((nota1 >= 7.0) and (nota2 >= 7.0) and (nota3 >= 7.0))

print('Aluno está aprovado? ' + str(situacao)) #Função str() converte valor para string
