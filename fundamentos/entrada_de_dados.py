"""
Entrada de dados

É o fornecimento de valores para um programa por meio de um dispositivo de entrada de dados (ex., teclado).

Em Python, a função input() permite que um usuário entre com os dados e estes dados sejam atribuídos a uma variável.
"""

x = input("Digite um número: ")
print(x)


# Para ler dados numéricos basta usar as funções int() e float() para converter uma string nesses valores.

ano = int(input('Ano de nascimento: '))
print('Sua idade: %d anos' % (2021 - ano))

altura = float(input('Altura: '))
print('Sua altura é: %4.2f m' % altura)
