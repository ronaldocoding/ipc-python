'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km)
e o total de combustível gasto (em litros).

<- ENTRADA
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km),
e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

-> SAÍDA
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula,
seguido da mensagem "km/l".
'''

X = int(input())
Y = float(input())
consumo = X/Y

print("{:.3f} km/l".format(consumo))
