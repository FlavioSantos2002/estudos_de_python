def main():
    #fazer a matriz
    #preencher a matriz
    lxc = input()
    a = lxc.split(' ')

    for vetor in range(len(a)):
        a[vetor] = int(a[vetor])
    

    matrix = [[0 for _ in range(a[1])] for _ in range(a[0])]

    for i in range(a[0]):
        
        b = input().split(' ') 
        for vetor in range(len(b)):
            b[vetor] = int(b[vetor])
        for j in range(len(b)):
            matrix[i][j] = b[j]

    #quantas peças de roupa vou tirar da matriz

    pr = int(input())


    #digitar as peças retiradas 
    pecas = 0
    for j in range(pr):
        lxc = input()
        q = lxc.split(" ")
        for vetor in range(len(q)):
            q[vetor] = int(q[vetor])
        if (matrix[q[0] - 1][q[1] - 1] != 0 ):
            matrix[q[0] - 1][q[1]- 1] = matrix[q[0] - 1][q[1]- 1] - 1
            pecas = pecas + 1

    print(pecas)
if __name__ == "__main__":
    main()

