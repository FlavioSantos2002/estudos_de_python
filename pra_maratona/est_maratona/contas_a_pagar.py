def main():
    #quanto ele tem
    v = int(input())

    #quanto ele deve pra açogue farmacia e padaria
    a = int(input())
    f = int(input())
    p = int(input())

    dividas = [a, f, p]

    #logica pra saber quanto ele consegue pagar
    if (sum(dividas) <= v):
        print(3)
    else:
        if(((a+f)<=v) or ((a+p)<=v) or ((p+f)<=v)):
            print(2)
        elif((a<=v) or (f<=v) or (p<=v)):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()