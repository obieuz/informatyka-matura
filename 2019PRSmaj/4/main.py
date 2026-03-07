from copy import deepcopy
from enum import Enum


class Typy(Enum):
    przeszkoda = "X"
    trawa = "*"
    puste = "."


def licz_jakie_typy(dzialka):
    przeszkody = 0
    trawa = 0
    puste = 0
    for i in range(len(dzialka)):
        for j in range(len(dzialka[i])):
            if dzialka[i][j] == Typy.przeszkoda.value:
                przeszkody += 1
            elif dzialka[i][j] == Typy.trawa.value:
                trawa += 1
            else:
                puste += 1
    return przeszkody, trawa, puste


def zadanie_4_1(dzialki):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        LICZBA_WSZYSTKICH_POL = 900
        cnt = 0
        for dzialka in dzialki:
            przeszkody, trawa, puste = licz_jakie_typy(dzialka)
            if trawa / LICZBA_WSZYSTKICH_POL >= 0.7:
                cnt += 1
        print(cnt, file=output_file)


def obrot_180(dzialka):
    for i in range(len(dzialka)):
        dzialka[i] = list(reversed(dzialka[i]))
    return list(reversed(dzialka))


# print(obrot_180([["D","B","C"],["C","D","A"]]))

def zadanie_4_2(dzialki):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        for i in range(len(dzialki)):
            for j in range(len(dzialki)):
                if i == j:
                    continue
                if dzialki[i] == obrot_180(dzialki[j]):
                    print(f"{i + 1} i {j + 1}", file=output_file)
                    break


def znajdz_przeszkody(dzialka):
    przeszkody = []
    for i in range(len(dzialka)):
        for j in range(len(dzialka[i])):
            if dzialka[i][j] == Typy.przeszkoda.value:
                przeszkody.append((j, i))
    return przeszkody


def czy_przeszkoda_w_polu(pos, bok, przeszkody):
    x_pola, y_pola = pos
    for przeszkoda in przeszkody:
        x_prze, y_prze = przeszkoda

        if x_pola <= x_prze <= x_pola + (bok - 1):
            if y_pola <= y_prze <= y_pola + (bok - 1):
                return True
    return False


def oblicz_dlugosc_boku_pola_bez_przeszkod(pos, dzialka, przeszkody):
    x, y = pos
    dlugosc_boku = 1

    while x + dlugosc_boku < len(dzialka) and czy_przeszkoda_w_polu(pos, dlugosc_boku + 1, przeszkody) == False:
        dlugosc_boku += 1
    return dlugosc_boku

def zadanie_4_3(dzialki):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        dlugosci_dzialek = dict()
        for index, dzialka in enumerate(dzialki):
            przeszkody = znajdz_przeszkody(dzialka)
            dlugosc_boku = oblicz_dlugosc_boku_pola_bez_przeszkod((0,0),dzialka,przeszkody)

            if dlugosc_boku not in dlugosci_dzialek:
                dlugosci_dzialek[dlugosc_boku] = [index+1]
            else:
                dlugosci_dzialek[dlugosc_boku].append(index+1)

        max_dlugosc = max(dlugosci_dzialek)
        print(f"maksymalny bok - {max_dlugosc}",file=output_file)
        for index_dzialki in dlugosci_dzialek[max_dlugosc]:
            print(f"numer dzialki - {index_dzialki}",file=output_file)


def main():
    with open("dzialki.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        dzialki = []
        for i in range(0, len(dane), 31):
            dzialki.append(dane[i:i + 30])
        zadanie_4_1(dzialki)
        dzialki_dwa = deepcopy(dzialki)
        zadanie_4_2(dzialki_dwa)
        zadanie_4_3(dzialki)


main()

