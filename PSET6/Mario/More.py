from cs50 import get_int


def main():
    while True:
        altura = get_int("Qual a altura da piramide?: ")
        largura = altura
        if largura >= 0 and altura <= 8:
            break

    for i in range(1, altura + 1):
        num_hashes = i
        num_espaco = largura - num_hashes

        print(" " * num_espaco, end="")
        print("#" * num_hashes, end="")

        print("  ", end="")

        print("#" * num_hashes)


if __name__ == "__main__":
    main()
