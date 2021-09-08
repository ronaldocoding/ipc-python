'''
o/ Iae pessoal, Tudo bem?
Espero que sim :)
Bom este é o exercício 1018 do URI, modulo iniciante

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

<-- Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

--> Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

'''


valor = int(input())
cedula = [100, 50, 20, 10, 5, 2, 1]           #lista usada para os tipos de cedula 100,50,20 e por ai
ncedula = [0, 0, 0, 0, 0, 0, 0]               #lista usada para receber as quantidades de cada tipo de cedula

valor_pre_calculado = 0                       #variavel para ajudar no calculo da quantidade das cedulas
print(valor)

for index in range(7):                        #laço de repeticão que roda enquanto a variavel index não chegar em 7
                                              #variável de indexação = Usada para rodar as listas e laços de maneira ordenada e sincrona
                                              #Em cada loop, a variável index somará mais 1 no seu valor, até chegar no valor estimado no range
                                              #EX: for index in range(5) -> index = 0; index = 1; index = 2; ...; index = 5

    ncedula[index] = int((valor - valor_pre_calculado) / cedula[index])         #calcula a quantidade de cada cedula, pegando somente o primeiro valor inteiro

    valor_pre_calculado = valor_pre_calculado + ncedula[index] * cedula[index]  #auxilia a calcular somente o dinheiro que já n foi calculado (tranformado em inteiro na ncedula)

    print(" {} nota(s) de R$ {},00".format(ncedula[index], cedula[index]))

'''
Caso ainda esteja dificil de entender o laço, tenho outro código fonte que não uso for
mas é mais complicado de entender hehe XD
tae para quem quiser ver

valor = int(input())

n100 = int(valor/100)
n50 = int((valor - n100*100)/50)
n20 = int((valor - (n100*100 + n50*50))/20)
n10 = int((valor - (n100*100 + n50*50 + n20*20))/10)
n5 = int((valor - (n100*100 + n50*50 + n20*20 + n10*10))/5)
n2 = int((valor - (n100*100 + n50*50 + n20*20 + n10*10 + n5*5))/2)
n1 = int((valor - (n100*100 + n50*50 + n10*20 + n10*10 + n5*5 + n2*2))/1)

print(valor)
print("%i nota(s) de R$ 100,00" %n100)
print("%i nota(s) de R$ 50,00" %n50)
print("%i nota(s) de R$ 20,00" %n20)
print("%i nota(s) de R$ 10,00" %n10)
print("%i nota(s) de R$ 5,00" %n5)
print("%i nota(s) de R$ 2,00" %n2)
print("%i nota(s) de R$ 1,00" %n1)

no fim, da no msm, mais consome mais memória '-'

Bons estudos e até o/

'''



