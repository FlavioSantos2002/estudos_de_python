def is_subsequence(sub, full):
    sub_index = 0  # Índice para percorrer a sequência sub
    for num in full:
        if num == sub[sub_index]:
            sub_index += 1
            if sub_index == len(sub):
                return True  # A sequência sub é uma subsequência da sequência full
    return False

def main():
    # Lendo as sequências S_A e S_B como listas de inteiros

    input()
    sequence_A = list(map(int, input().split()))
    sequence_B = list(map(int, input().split()))

    # Verificando se S_B é uma subsequência de S_A
    if is_subsequence(sequence_B, sequence_A):
        print("S")
    else:
        print("N")


if __name__ == "__main__":
    main()


    