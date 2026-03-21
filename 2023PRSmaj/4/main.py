from collections import Counter


def zadanie_4_1(data):
    with open("wyniki4_1.txt", "w") as output_file:
        for row in data:
            counter = Counter(row)
            if counter["w"] == counter["k"]:
                print(row, file=output_file)

COUNTER_WAKACJE = Counter("wakacje")

def ile_powt(slowo):
    counter = Counter(slowo)

    ile_powt_dict = dict()

    for key, value in COUNTER_WAKACJE.items():
        powt = counter[key] // COUNTER_WAKACJE[key]

        if powt == 0:
            return 0
        if key not in ile_powt_dict:
            ile_powt_dict[key] = powt

    return min(ile_powt_dict.values())


def zadanie_4_2(data):
    with open("wyniki4_2.txt", "w") as output_file:
        for row in data:
            print(ile_powt(row),end=" ",file=output_file)

# print(ile_powt("wwwaaaaakkcccjjee"))

BASE_WORD = "wakacje"

def ile_poprawek(slowo):
    liczba_usuniec = 0
    liczba_usun_do_zera = len(slowo)
    slowo_ost = ""
    i = 0
    j = 0
    czy_koniec_slowa = False
    enum_wakacje = []

    while not czy_koniec_slowa:
        while j < len(slowo):
            if BASE_WORD[i%len(BASE_WORD)] == slowo[j]:
                slowo_ost = slowo_ost + BASE_WORD[i%len(BASE_WORD)]
                i += 1
                j += 1

                if len(slowo_ost) / len(BASE_WORD) == int(len(slowo_ost) / len(BASE_WORD)):
                    enum_wakacje.append(liczba_usuniec + len(slowo) - j)
                    # print(slowo_ost, liczba_usuniec + len(slowo) - j)

                break
            liczba_usuniec += 1
            # print(BASE_WORD[i%len(BASE_WORD)], slowo[j], liczba_usuniec)
            j += 1

        if j == len(slowo):
            czy_koniec_slowa = True
    if ile_powt(slowo_ost)==0:
        return liczba_usun_do_zera
    if min(enum_wakacje) < liczba_usun_do_zera:
        return min(enum_wakacje)
    return liczba_usun_do_zera

# print(ile_poprawek("uwlccorhlvfnnuleavntzuqalkrajcsnlwlynncrsmvfejqjvxnntlljxxekaeptexfubclfsarlbkvwhtxzwakdhselohpejjty")) #93

# print(ile_powt("uwlccorhlvfnnuleavntzuqalkrajcsnlwlynncrsmvfejqjvxnntlljxxekaeptexfubclfsarlbkvwhtxzwakdhselohpejjty"))


def zadanie_4_3(data):
    with open("wyniki4_3.txt", "w") as output_file:
        for row in data:
            print(ile_poprawek(row), end=" ", file=output_file)

def main():
    with open("slowa.txt", "r") as file:
        data = file.read().split("\n")[:-1]
        # print(data)
        zadanie_4_1(data)
        zadanie_4_2(data)
        zadanie_4_3(data)

main()
