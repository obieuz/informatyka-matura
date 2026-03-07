from collections import Counter


def czy_prawie_zrownowazona(liczba, margines_zmian=1):
    counter = Counter(liczba)
    if abs(counter["0"] - counter["1"]) == margines_zmian:
        return True
    return False


def czy_zrownowazona(liczba):
    if len(liczba) % 2 == 1:
        return False
    return czy_prawie_zrownowazona(liczba, 0)


def zadanie_4_1(dane):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        cnt_zrow = 0
        cnt_praw_zrow = 0
        for liczba in dane:
            if czy_zrownowazona(liczba):
                cnt_zrow += 1
            if czy_prawie_zrownowazona(liczba):
                cnt_praw_zrow += 1
        print(cnt_zrow, cnt_praw_zrow, sep="\n", file=output_file)


def silnia(n):
    iloraz = 1
    for i in range(1, n + 1):
        iloraz *= i
    return iloraz


# print(silnia(5))


def licz_anagramy(liczba):
    liczba = liczba[1:]
    counter = Counter(liczba)
    return int(silnia(len(liczba)) / (silnia(counter["0"]) * silnia(len(liczba) - counter["0"])))


# print(licz_anagramy("11100"))
# print(licz_anagramy("10001011"))

def zadanie_4_2(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        liczby = dict()
        for liczba in dane:
            if len(liczba) != 8:
                continue
            anagramy = licz_anagramy(liczba)
            if anagramy in liczby:
                liczby[anagramy].append(liczba)
            else:
                liczby[anagramy] = [liczba]
        max_anagramy = max(liczby)
        for value in liczby.get(max_anagramy):
            print(value, file=output_file)


def zadanie_4_3(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        max_diffrence = abs(int(dane[0], 2) - int(dane[1], 2))
        for i in range(1, len(dane) - 1):
            curr_diffrence = abs(int(dane[i], 2) - int(dane[i + 1], 2))

            if max_diffrence < curr_diffrence:
                max_diffrence = curr_diffrence
        print(str(bin(max_diffrence))[2:], file=output_file)


def get_cyfry(liczba):
    cyfry = set()
    for cyfra in str(liczba):
        cyfry.add(int(cyfra))
    return cyfry


def zadanie_4_4(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.4", file=output_file)
        cnt = 0
        max_diffrence = sum(get_cyfry(int(dane[0], 2)))
        max_diffrence_digit = int(dane[0], 2)
        for liczba in dane:
            liczba = int(liczba, 2)
            cyfry = get_cyfry(liczba)

            if 0 not in cyfry:
                cnt += 1

            curr_diffrence = sum(cyfry)

            if curr_diffrence > max_diffrence:
                max_diffrence = curr_diffrence
                max_diffrence_digit = liczba
        print(cnt, file=output_file)
        print(max_diffrence_digit, file=output_file)


def main():
    with open("anagram.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
        zadanie_4_4(dane)
        # print(dane)


main()
