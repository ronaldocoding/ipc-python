'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor
a ser pago.

<- ENTRADA
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente
dois inteiros e um valor com 2 casas decimais.

-> SAÍDA
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois
pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

peca1 = input() .split() # peca1 é a variavel que recebe o input com os 3 valores, e o .split() divide esses valores em linhas
cod1 = int(peca1[0])
np1 = int(peca1[1])
val1 = float(peca1[2])
# cada um representa uma linha da variavel peca1, em int(peca[x]) definimos a posição que cada valor vai ocupar e o seu tipo.

peca2 = input() .split()
cod2 = int(peca2[0])
np2 = int(peca2[1])
val2 = float(peca2[2])

total = (np1 * val1) + (np2 * val2) #calcula o valor total na compra das duas peças

print("VALOR A PAGAR: R$ {:.2f}".format(total))
