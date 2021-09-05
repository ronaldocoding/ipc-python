m = []
ns = []
while True:
    try:
        n = int(input())
    except:
        break
    else:
        ns.append(n)

for n in ns:
    for i in range(0, n):
        for j in range (0, n):
            if(i==n-1-j):
                print('2', end="")
            elif(i==j):
                print('1', end="")
            else:
                print('3', end="")
        print('')
