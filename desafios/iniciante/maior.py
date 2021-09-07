'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula: maiorAB = (a+b + abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário
para chegar no resultado esperado.

<- ENTRADA
O arquivo de entrada contém três valores inteiros.

-> SAÍDA
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
valores = input() .split()
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
maiorAB = (A + B + abs(A-B))/2 #função abs() retorna o valor absoluto do resultado da subtração entre A e B. O módulo na matemática
maior = (maiorAB + C + abs(maiorAB - C))/2

print("{} eh o maior".format(int(maior)))
