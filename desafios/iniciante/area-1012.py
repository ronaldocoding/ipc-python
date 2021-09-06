'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida,
calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

<- ENTRADA
 O arquivo de entrada contém três valores com um dígito após o ponto decimal.

-> SAÍDA
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre
com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado
com 3 dígitos após o ponto decimal.
'''

valor = input() .split()
A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
pi = 3.14159

atriangulo = (A * C)/2 # formula da area do triango base*altura/2
acirculo = pi * C**2 # formula da area do circulo pi*raio ao quadrado
atrapezio = ((A + B) * C)/ 2 #formula da area do trapezio (base + base) * altura /2
aquadrado = B**2  #formula da area do quadrado lado*lado
aretangulo = A * B

print("TRIANGULO: {:.3f}".format(atriangulo)) # {:.3f} define 3 casas decimais na saída | ex: 4.123
print("CIRCULO: {:.3f}".format(acirculo))
print("TRAPEZIO: {:.3f}".format(atrapezio))
print("QUADRADO: {:.3f}".format(aquadrado))
print("TRIANGULO: {:.3f}".format(aretangulo))