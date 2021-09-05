# Link do desafio: https://www.urionlinejudge.com.br/judge/en/problems/view/1022
# 1. Ler a quantidade de casos(expressões) que serão testadas 1 <= N <= 10**4 
# 2. Ler as N expressões no formato: 
# Ex: 1 / 2 + 3 / 4
# 3. Calcular valor das expressões
# 4. Apresentar valor calculado de forma que apresente também os valores simplificados
# Ex: 10/8 = 5/4

from re import findall, search # Biblioteca padrão para trabalhar com Regex
from fractions import Fraction # Biblioteca padrão para trabalhar com frações

def calcular_expressao(expressao):
    numeros_strings = findall("[0-9]+", expressao)
    operacao = findall("[+-/*]", expressao)[1]
    numeros = [int(n) for n in numeros_strings]

    for n in numeros: # Valida tamanho dos números 
        if not 1 <= n <= 1000:
            exit(0)

    N1, D1, N2, D2 = numeros # Desestrutura o vetor de números em 4 variáveis separadas

    if operacao == '+':
        NResultado = N1*D2 + N2*D1
        DResultado = D1*D2
    elif operacao == '-':
        NResultado = N1*D2 - N2*D1
        DResultado = D1*D2
    elif operacao == '*':
        NResultado = N1*N2
        DResultado = D1*D2
    elif operacao == '/':
        NResultado = N1*D2
        DResultado = N2*D1

    fracaoRedutivel = Fraction(NResultado, DResultado)

    NResultadoSimplificado = fracaoRedutivel.numerator
    DResultadoSimplificado = fracaoRedutivel.denominator

    resultado = f"{NResultado}/{DResultado} = {NResultadoSimplificado}/{DResultadoSimplificado}" # Formata resultado com as frações na forma irredutível
    
    print(resultado) # Apresenta resultado da operação

def valida_expressao(expressao):
    e_valido = search("[0-9]+ / [0-9]+ [+-/*] [0-9]+ / [0-9]+", expressao) # Valida expressão utilizando Regex (https://en.wikipedia.org/wiki/Regular_expression)
    if e_valido:
        return True
    return False

def principal():
    N = int(input()) # Ler número N (Quantidade de expressões que serão solicitadas)
    
    if not 1 <= N <=10**4: # Valida número N
        exit(0)
    
    expressoes = []
    
    for Nx in range(N):
        expressao = input() # Ler expressão
    
        if not valida_expressao(expressao): # Validação da expressão
            exit(0)
    
        expressoes.append(expressao) # Se verdadeiro, adiciona ao vetor de expressões

    for Nx in range(N):
        calcular_expressao(expressoes[Nx])

principal() # Executa programa