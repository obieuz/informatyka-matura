SCREEN_WIDTH = 320
SCREEN_HEIGHT = 200


def zadanie_6_1(piksele):
    with open("wyniki6.txt", "w") as output_file:
        print("6.1", file=output_file)
        max_value = int(piksele[0][0])
        min_value = int(piksele[0][0])
        for i in range(SCREEN_HEIGHT):
            for j in range(SCREEN_WIDTH):
                piksel = int(piksele[i][j])

                if piksel > max_value:
                    max_value = piksel
                if piksel < min_value:
                    min_value = piksel
        print(max_value, min_value, sep=" i ", file=output_file)


def czy_wiersz_do_usuniecia(wiersz):
    i = 0
    j = -1
    while i < len(wiersz) // 2:
        if wiersz[i] != wiersz[j]:
            return True
        i += 1
        j -= 1
    return False


# print(czy_wiersz_do_usuniecia(["0","1","0"]))
# print(czy_wiersz_do_usuniecia(["1","1","0"]))
# print(czy_wiersz_do_usuniecia(["1","0","0","1"]))

def zadanie_6_2(piksele):
    with open("wyniki6.txt", "a") as output_file:
        print("6.2", file=output_file)
        cnt = 0
        for row in piksele:
            if czy_wiersz_do_usuniecia(row):
                cnt += 1
        print(cnt, file=output_file)


def czy_konstrastujacy_sasiedni(x, y, piksele, value_piksela):
    for j in range(x - 1, x + 2, 2):
        if j < 0:
            continue
        if j >= SCREEN_WIDTH:
            continue
        if abs(int(piksele[y][j]) - value_piksela) > 128:
            return True

    for i in range(y - 1, y + 2, 2):
        if i < 0:
            continue
        if i >= SCREEN_HEIGHT:
            continue
        if abs(int(piksele[i][x]) - value_piksela) > 128:
            return True

    return False


def zadanie_6_3(piksele):
    with open("wyniki6.txt", "a") as output_file:
        print("6.3", file=output_file)
        cnt = 0
        for i in range(SCREEN_HEIGHT):
            for j in range(SCREEN_WIDTH):
                piksel = int(piksele[i][j])

                if czy_konstrastujacy_sasiedni(j, i, piksele, piksel):
                    cnt += 1
        print(cnt, file=output_file)


def oblicz_najd_ciag_jasn_pik(x_index, piksele):
    max_ciag = 1
    curr_ciag = 1
    for j in range(SCREEN_HEIGHT - 1):
        if piksele[j][x_index] == piksele[j + 1][x_index]:
            curr_ciag += 1
            if max_ciag < curr_ciag:
                max_ciag = curr_ciag
        else:
            curr_ciag = 1
    return max_ciag


# print(oblicz_najd_ciag_jasn_pik(["0","0","1","0","0","0","0","1","2"]))

def zadanie_6_4(piksele):
    with open("wyniki6.txt", "a") as output_file:
        print("6.4", file=output_file)
        max_ciag = oblicz_najd_ciag_jasn_pik(0, piksele)
        for i in range(1, SCREEN_WIDTH):
            curr = oblicz_najd_ciag_jasn_pik(i, piksele)

            if max_ciag < curr:
                max_ciag = curr
        print(max_ciag, file=output_file)


def main():
    with open("dane.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        piksele = []
        for row in dane:
            piksele.append(row.split(" "))

        zadanie_6_1(piksele)
        zadanie_6_2(piksele)
        zadanie_6_3(piksele)
        zadanie_6_4(piksele)


main()
