from cs50 import get_int

altura = 0

while (altura<=0 or altura >8):
    altura = get_int("Qual a altura da piramide? ")

for row in range(altura):
    for space in range(altura - row - 1, 0, -1):
        print(" ", end="")
    for hash in range(row+1):
        print("#", end="")
    print("\n", end="")
