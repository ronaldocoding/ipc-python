"""
Em Python há quatro tipos:

    1. int (inteiro): 4, -3, 0
    2. float (real): 4.0, -3.0, 1024.5
    3. str ("string" ou cadeia de caracteres): "4.0", "Ronaldo, "João"
    4. bool (booleana ou lógico): True e False

Variáveis são valores armazenados em endereços de memória. Estão associados a um tipo de dado e seu valor pode ser
mudado. São definidas no momento em que valores são atribuídos a elas pelo comando "=".
"""

inteiro = 10
pFlutuante = 10.5 #ponto flutuante -> float
nome = "Ronaldo"
booleano = True

#O comando type() retorna o tipo da variável
print(type(inteiro))
print(type(pFlutuante))
print(type(nome))
print(type(booleano))
"""
Output:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
"""

""""
Operadores são símbolos especiais que aplicam uma computação sobre alguns dados, denominados operandos.
    
    Operadores numéricos:
    
    1. ** (exponenciação)
    2. % (módulo ou resto da divisão inteira)
    3. * (multiplicação)
    4. / (divisão)
    
Precedência entre esses operadores: () > ** > % > # > + -
"""

print(10 ** 2) #100
print(10 % 2) #O resto da divisão entre 10 e 2 é 0
print(10 + 2) #12
print(10 - 2) #8

"""
Operadores de atribuição:

    1. = (atribuição simples): x = 3
    2. Múltiplas atribuições: x = 3; y = x + 4; z = x * y
    3. Atribuição múltipla: x, y, z = 1, 2, 3
"""

a = 4
b = 5; c = b + 6; d = b * c
x, y, z = 1, 2, 3

print(a , b, c, d, x, y, z)

"""
Output

4 5 11 55 1 2 3
"""

"""
Operadores relacionais expressam igualdade e desigualdade. Eles resultam em um valor lógico: True ou False

    1. == (igualdade)
    2. != (diferença)
    3. > (maior) e >= (maior ou igual)
    4. < (menor) e <= (menor ou igual)
"""

print(10 == 10) #True
print(10 == 2) #False
print(10 != 2) #True
print(10 != 10) #False
print(10 > 2) #True
print(10 > 12) #False
print(10 >= 2) #True
print(10 >= 12) #False
print(10 < 12) #True
print(10 < 2) #False
print(10 <= 12) #True
print(10 <= 2) #False

"""
Operadores lógicos resultam também em um valor lógico

    1. not (não, negação)
    2. or (ou, disjunção)
    3. and (e, conjunção)
    
Ordem de precedência: () > not > and > or
"""

#Resultado será False (falso) já que é a negação de uma verdade
print(not 10 == 10)

#Resultado será True (verdadeiro) já que é a negação de uma falsidade
print(not 10 == 2)
