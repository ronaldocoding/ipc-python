"""
Variáveis string

Uma string é uma sequência de caracteres delimitada por aspas duplsa("") ou aspas simples (''). Cada caractere de uma
string pode ser acessado separadamente pode meio de um índice que se inicia em 0 (zero).
"""

frase = 'Python é legal!'
print(frase[0]) # Imprime 'P'
print(frase[5]) # Imprime 'n'

# A função len() retorna o tamanho (lenght) de um string

print(len(frase)) # Imprime 15

# As strings podem ser "somadas" (concatenadas) com o operador + (soma)

print(frase + ' Mas Javascript é melhor.')

# Output
# Python é legal! Mas Javascript é melhor.

# Strings podem ser "multiplicadas" (repetidas 0 ou mais vezes) com o operador * (multiplicação)

print('Python ' * 3)

# Output
# Python Python Python

# O operador % pode compor valores do tipo int, float e str em uma string.

ano = 1989

print('Python foi criado em %d' % (ano))

# Output
# Python foi criado em 1989

# Os marcadores utilizados na composição são os seguintes: %d, para int, %s, para string e %f para float

# Os marcadores %d e %f têm parâmetros de formatação adicionais.

idade = 21
print('[%05d]' % idade) # Imprime idade como um número de 5 dígitos, adicionando 3 zeros à esquerda

# Output
# [00021]

# Outros exemplos

print('[%-5d]' % idade)
print('R$%5.2f' % 52.75) # Imprime como um número de 5 dígitos e adiciona o símbolo do real

# Output
# [21   ]
# R$52.75

# O operador ":" retorna uma fatia p:q de uma string, que vai da posição p até a posição q - 1 da string

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(s[0:3]) # Imprime ABC
print(s[1:3]) # Imprime BC
print(s[:5]) # Do início até 4 (5 - 1)
print(s[0:]) # De 0 até o fim
print(s[:-1]) # Do início até o penúltimo

# Output
# ABCDE
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXY