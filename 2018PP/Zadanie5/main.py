def zadanie_1(liczby):
    with open("wyniki5.txt", "w") as output_file:
        print("1", file=output_file)
        max = 0
        czy_pierwsze = True
        for liczba in liczby:
            if liczba % 2 != 0:
                continue

            if czy_pierwsze:
                max = liczba
                czy_pierwsze = False
                continue

            if not max < liczba:
                continue

            max = liczba

        print(max, file=output_file)


def czy_palindrom(liczba_str):
    if len(liczba_str) == 1:
        return True

    for i in range(len(liczba_str) // 2):
        if liczba_str[i] != liczba_str[-i-1]:
            return False
    return True

# print(czy_palindrom("23432")) # True
# print(czy_palindrom("34334")) # False
# print(czy_palindrom("5665")) # True
# print(czy_palindrom("1234")) # False


def zadanie_2(dane):
    with open("wyniki5.txt", "a") as output_file:
        print("2", file=output_file)
        for liczba_str in dane:
            if not czy_palindrom(liczba_str):
                continue

            print(liczba_str,file=output_file)

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra
        liczba //= 10
    return suma

# print(suma_cyfr(12)) #3
# print(suma_cyfr(2)) #2
# print(suma_cyfr(300)) #3



def zadanie_3(liczby):
    with open("wyniki5.txt", "a") as output_file:
        print("3", file=output_file)
        suma = 0
        for liczba in liczby:
            suma_cyfr_liczby = suma_cyfr(liczba)
            suma += suma_cyfr_liczby

            if not suma_cyfr_liczby > 30:
                continue

            print(liczba, file=output_file)


        print(f"Suma cyfr --- {suma}", file=output_file)


def main():
    with open("liczby.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        liczby = [int(i) for i in dane]

        zadanie_1(liczby)
        zadanie_2(dane)
        zadanie_3(liczby)


main()
