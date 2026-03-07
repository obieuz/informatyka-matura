from copy import deepcopy
from enum import Enum


class Typ_Komorki(Enum):
    zyjaca = "X"
    martwa = "."


def znajdz_zyjace_komorki(plansza) -> list[tuple]:
    pozycje_zyjacych_komorek = []
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] == "X":
                pozycje_zyjacych_komorek.append((j, i))
    return pozycje_zyjacych_komorek


def znajdz_sasiadow(plansza, pos: tuple):
    x, y = pos
    martwi_sasiedzi = []
    zywi_sasiedzi = []
    for i in range(y - 1, y + 2):
        i %= len(plansza)
        for j in range(x - 1, x + 2):
            j %= len(plansza[i])
            if i==y and x == j:
                continue
            if plansza[i][j] == "X":
                zywi_sasiedzi.append((j, i))
            else:
                martwi_sasiedzi.append((j, i))
    return martwi_sasiedzi, zywi_sasiedzi

# print(znajdz_sasiadow([[".","X","X","."],["X",".","X","."],["X",".","X","."]],(1,1)))

def zmien_status_pola(plansza, pos: tuple, znak):
    x, y = pos
    plansza[y][x] = znak


# print(znajdz_zyjace_komorki([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.',
# '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.',
# '.', '.', '.', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.',
# '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.',
# '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
# '.', '.', '.']]))

def symuluj_runde(plansza):
    nowa_plansza = deepcopy(plansza)

    pozycje_zyjacych_komorek = znajdz_zyjace_komorki(plansza)

    martwi_sasiedzi_zyjacych_komorek = []

    for zyjaca_komorka in pozycje_zyjacych_komorek:
        martwi_sasiedzi, zywi_sasiedzi = znajdz_sasiadow(plansza, zyjaca_komorka)

        martwi_sasiedzi_zyjacych_komorek.extend(martwi_sasiedzi)
        if len(zywi_sasiedzi) not in [2, 3]:
            zmien_status_pola(nowa_plansza, zyjaca_komorka, Typ_Komorki.martwa.value)



    for martwa_komorka in martwi_sasiedzi_zyjacych_komorek:
        martwi_sasiedzi, zywi_sasiedzi = znajdz_sasiadow(plansza, martwa_komorka)

        if len(zywi_sasiedzi) == 3:
            zmien_status_pola(nowa_plansza, martwa_komorka, Typ_Komorki.zyjaca.value)

    return nowa_plansza

def symuluj_n_rund(n, plansza):
    plansza_po_sym = plansza
    for i in range(n):
        plansza_po_sym = symuluj_runde(plansza_po_sym)
    return plansza_po_sym


# print(znajdz_zyjace_komorki(symuluj_n_rund(11, [
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']])))


def konwertuj_na_plansze(text):
    rekordy_planszy = text.split("\n")
    plansza = []
    for rekord in rekordy_planszy:
        tablica_wyjsciowa = []
        for znak in rekord:
            tablica_wyjsciowa.append(znak)
        plansza.append(tablica_wyjsciowa)
    return plansza


def zadanie_5_1(plansza):
    with open("wyniki_5.txt","w") as output_file:
        print("5.1",file=output_file)
        plansza_po_symulacji = symuluj_n_rund(36,plansza)
        martwi, zywi = znajdz_sasiadow(plansza_po_symulacji,(19-1,2-1))
        print(len(zywi),file=output_file)

def zadanie_5_2(plansza):
    with open("wyniki_5.txt","a") as output_file:
        print("5.2", file=output_file)
        plansza_po_symulacji = symuluj_n_rund(1,plansza)
        zyjace_komorki = znajdz_zyjace_komorki(plansza_po_symulacji)
        print(len(zyjace_komorki),file=output_file)

def zadanie_5_3(plansza):
    with open("wyniki_5.txt","a") as output_file:
        print("5.3", file=output_file)
        poprzednia_ilosc_zyjacych_komorek = znajdz_zyjace_komorki(plansza)
        pokolenie = 0
        for i in range(1,100):
            plansza_po_symulacji = symuluj_n_rund(i,plansza)
            zyjace_komorki = znajdz_zyjace_komorki(plansza_po_symulacji)
            if poprzednia_ilosc_zyjacych_komorek == zyjace_komorki:
                pokolenie = i+1
                break
            else:
                poprzednia_ilosc_zyjacych_komorek = zyjace_komorki
        print(f"Jest to {pokolenie} pokolenie",file=output_file)
        print(f"Zywych komorek w tym pokoleniu bylo {len(poprzednia_ilosc_zyjacych_komorek)}",file=output_file)



def main():
    with open("gra.txt", "r") as file:
        plansza = konwertuj_na_plansze(file.read())
        zadanie_5_1(plansza)
        zadanie_5_2(plansza)
        zadanie_5_3(plansza)
main()
