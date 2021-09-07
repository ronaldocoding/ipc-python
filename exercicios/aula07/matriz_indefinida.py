'''
2) Escreva um programa que imprima na tela

1,1 1,2 1,3 ... 1,n
2,1 2,2 2,3 ... 2,n
 .   .   .  .
 .   .   .    .
m,1 m,2 m,3 ... m,n

onde n,m são inteiros positivos informados por
um usuário.
'''

m = (int(input("Insira um valor para 'm': ")))
n = (int(input("Insira um valor para 'n': ")))

linhas = 1
colunas = 1

while linhas <= m: # Do 1 até o m

    linha = "" # String onde ficarão os valores de cada linha

    while colunas <= n: # Do x,1 até o x,n
        linha += str(linhas) + "," + str(colunas) + " "
        colunas += 1

    print(linha)

    linhas += 1
    colunas = 1 # Reiniciar a contagem dos valores de cada linha
    del linha # Deleta-se a linha para reiniciar a escrita dos valores