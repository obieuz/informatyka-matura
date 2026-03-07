def czy_pierwsza(liczba):
    if liczba == 1:
        return False
    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True


def zadanie_4_1(liczby):
    with open("wyniki4_1.txt", "w") as output_file:
        min_liczba = -1
        max_liczba = -1
        cnt = 0
        for liczba in liczby:
            liczba = int(liczba)
            if czy_pierwsza(liczba):
                cnt += 1
                if liczba > max_liczba:
                    max_liczba = liczba
                if liczba < min_liczba or min_liczba == -1:
                    min_liczba = liczba
        print(f"Liczba liczb pierwszych {cnt}", file=output_file)
        print(f"Najwieksza liczba {max_liczba}", file=output_file)
        print(f"Najmniejsza liczba {min_liczba}", file=output_file)


def czy_palindrom(liczba_bin):
    i = 0
    j = -1
    while i < len(liczba_bin):
        if liczba_bin[i] != liczba_bin[j]:
            return False
        i += 1
        j -= 1
    return True


# print(czy_palindrom("1101011"))
# print(czy_palindrom("1110011"))

def czy_prawie_palindrom(liczba_bin: str):
    liczba_bin = liczba_bin.rstrip("0")
    return czy_palindrom(liczba_bin)


# print(czy_prawie_palindrom("11101110"))
# print(czy_prawie_palindrom("111011100"))

def zadanie_4_2(liczby):
    with open("wyniki4_2.txt", "w") as output_file:
        cnt = 0
        for liczba in liczby:
            liczba_bin = str(bin(int(liczba)))[2:]

            if czy_palindrom(liczba_bin) or czy_prawie_palindrom(liczba_bin):
                cnt += 1

        print(f"{cnt}", file=output_file)


# def get_set_cyfr(liczba):
#     cyfry = set()
#     for cyfra in liczba:
#         cyfry.add(cyfra)
#     return cyfry


def zadanie_4_3(liczby):
    with open("wyniki4_3.txt", "w") as output_file:
        cnt = 0
        # uzyte = []
        for i in range(len(liczby)):
            for j in range(len(liczby)):
                if i == j:
                    continue
                # if {i,j} in uzyte:
                #     continue
                if set(liczby[i]) == set(liczby[j]):
                    # uzyte.append({i,j})
                    cnt += 1

        print(f"{cnt//2}", file=output_file)

def main():
    with open("dane.txt", "r") as file:
        liczby = file.read().split("\n")[:-1]
        zadanie_4_1(liczby)
        zadanie_4_2(liczby)
        zadanie_4_3(liczby)


main()
