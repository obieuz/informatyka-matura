def get_x_y(row):
    row = row.split(" ")
    return int(row[0]), int(row[1])


def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True


# print(czy_pierwsza(5))


def zadanie_4_1(punkty):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        cnt = 0
        for punkt in punkty:
            x, y = get_x_y(punkt)
            if czy_pierwsza(x) and czy_pierwsza(y):
                cnt += 1
        print(cnt, file=output_file)


def get_set_cyfr(liczba):
    cyfry = set()
    for cyfra in str(liczba):
        cyfry.add(cyfra)
    return cyfry


def czy_cyfropodobna(x, y):
    if get_set_cyfr(x) == get_set_cyfr(y):
        return True
    return False


def zadanie_4_2(punkty):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        cnt = 0
        for punkt in punkty:
            x, y = get_x_y(punkt)
            if czy_cyfropodobna(x, y):
                cnt += 1
        print(cnt, file=output_file)


from math import sqrt


def get_odleglosc(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2

    return int(sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2)))


# print(get_odleglosc((1,1),(1,1)))
# print(get_odleglosc((3,2),(1,1)))

def zadanie_4_3(punkty):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        punkty_max = [get_x_y(punkty[0]), get_x_y(punkty[1])]
        odleglosc_max = get_odleglosc(punkty_max[0], punkty_max[1])
        for i in range(len(punkty)):
            for j in range(len(punkty)):
                if i == j:
                    continue

                punkt1 = get_x_y(punkty[i])
                punkt2 = get_x_y(punkty[j])
                odleglosc = get_odleglosc(punkt1, punkt2)

                if odleglosc > odleglosc_max:
                    punkty_max = [punkt1, punkt2]
                    odleglosc_max = odleglosc
        print(punkty_max[0], punkty_max[1], sep=", ", file=output_file)
        print(odleglosc_max, file=output_file)


GRANICA_MIN_X = 0
GRANICA_MAX_X = 5000
GRANICA_MIN_Y = -5000
GRANICA_MAX_Y = 5000


def czy_wewnatrz_kwadratu_bez_bokow(pos):
    x, y = pos
    if GRANICA_MIN_X < x < GRANICA_MAX_X:
        if GRANICA_MIN_Y < y < GRANICA_MAX_Y:
            return True
    return False


def czy_na_bokach_kwadratu(pos):
    x, y = pos
    if x == GRANICA_MIN_X or x == GRANICA_MAX_X:
        if GRANICA_MIN_Y <= y <= GRANICA_MAX_Y:
            return True
    if y == GRANICA_MIN_Y or y == GRANICA_MAX_Y:
        if GRANICA_MIN_X <= x <= GRANICA_MAX_X:
            return True
    return False


def czy_na_zewnatrz(pos):
    if czy_na_bokach_kwadratu(pos) == False and czy_wewnatrz_kwadratu_bez_bokow(pos) == False:
        return True
    return False


# print(czy_na_zewnatrz((6,5)))
# print(czy_na_zewnatrz((5,5)))
# print(czy_wewnatrz_kwadratu_bez_bokow((4,4)))


def zadanie_4_4(punkty):
    with open("wyniki4.txt", "a") as output_file:
        print("4.4", file=output_file)
        wewn_cnt = 0
        zewn_cnt = 0
        na_cnt = 0
        for punkt in punkty:
            pos = get_x_y(punkt)
            if czy_na_zewnatrz(pos):
                zewn_cnt += 1
            elif czy_wewnatrz_kwadratu_bez_bokow(pos):
                wewn_cnt += 1
            elif czy_na_bokach_kwadratu(pos):
                na_cnt += 1

        print(f"a. {wewn_cnt}", file=output_file)
        print(f"b. {na_cnt}", file=output_file)
        print(f"c. {zewn_cnt}", file=output_file)


def main():
    with open("punkty.txt", "r") as file:
        punkty = file.read().split("\n")[:-1]
        zadanie_4_1(punkty)
        zadanie_4_2(punkty)
        zadanie_4_3(punkty)
        zadanie_4_4(punkty)
        # print(punkty)

main()
