'''
3) Escreva um programa que simule a emissão de
dinheiro de uma máquina de caixa eletrônico.
Para um valor em dinheiro solicitado pelo cliente,
o programa deve mostrar na tela quais cédulas (de
100, 50, 20, 10, 5, 2, e 1) e quantas de cada,
devem ser ejetadas pela máquina. Considere que a
máquina tentará selecionar as cédulas em ordem
decrescente (das maiores para as menores
cédulas), e que o valor informado pelo usuário é
inteiro.
'''

total = (int(input("Qual valor deseja sacar? ")))

if total >= 100: # Se for um valor maior ou igual a 100 reais
    print("Total de cédulas de R$100,00: ", int(total/100))
    total -= 100 * int(total/100)

if total >= 50: # Se for um valor maior ou igual a 50 reais
    print("Total de cédulas de R$50,00: 1")
    # É impossível dar mais de uma cédula de R$50,00 , caso contrário seria uma de R$100,00
    total -= 50

if total >= 20: # Se for um valor maior ou igual a 20 reais
    print("Total de cédulas de R$20,00: ", int(total/20))
    total -= 20 * int(total/20)

if total >= 10: # Se for um valor maior ou igual a 10 reais
    print("Total de cédulas de R$10,00: ", int(total/10))
    total -= 10 * int(total/10)

if total >= 5: # Se for um valor maior ou igual a 5 reais
    print("Total de cédulas de R$5,00: ", int(total/5))
    total -= 5 * int(total/5)

if total >= 2: # Se for um valor maior ou igual a 2 reais
    print("Total de cédulas de R$2,00: ", int(total/2))
    total -= 2 * int(total/2)

if total >= 1: # Se for um valor maior ou igual a 1 real, apesar de não produzirem mais essa cédula...
    print("Total de cédulas de R$1,00: ", int(total))