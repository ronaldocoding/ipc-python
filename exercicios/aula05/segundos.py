'''
3) Escreva um programa que leia a quantidade de
dias, horas, minutos e segundos do usuário.
Calcule o total em segundos (1 min. = 60s; 1h =
60min; 1 dia = 24h).
'''

dias = (int(input("Número de dias: ")))
horas = (int(input("Número de horas: ")))
minutos = (int(input("Número de minutos: ")))
segundos = (int(input("Número de segundos: ")))

total_segundos = segundos
total_segundos += minutos*60      # Converter horas em segundos
total_segundos += horas*60*60     # Converter minutos em segundos
total_segundos += dias*24*60*60   # Converter dias em segundos

print("Total em segundos: ", total_segundos)