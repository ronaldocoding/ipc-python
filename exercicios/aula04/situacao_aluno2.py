"""
Acrescente ao problema anterior o fato de que para ser aprovado o aluno também deve ter uma frequência de pelo menos 75%
do total de aulas. O total de aulas é 60 horas-aula.
"""

nota1 = float(input('Nota 1: ')) #Recebe nota1 do usuário
nota2 = float(input('Nota 2: ')) #Recebe nota2 do usuário
nota3 = float(input('Nota 3: ')) ##Recebe nota3 do usuário
frequencia = int(input('Frequência (horas-aula): ')) #Recebe a frequência em horas-aula

situacao = ((nota1 >= 7.0) and (nota2 >= 7.0) and (nota3 >= 7.0) and (frequencia >= (0.75 * 60)))

print('Aluno está aprovado? ' + str(situacao)) #Função str() converte valor para string
