def zadanie_6_1(data):
    with open("wyniki_6_1.txt", "w") as output_file:
        cnt = 0
        for kod in data:
            if kod[-1] == "8":
                cnt += 1
        print(cnt, file=output_file)


def zadanie_6_2(data):
    with open("wyniki_6_2.txt", "w") as output_file:
        cnt = 0
        for kod in data:
            if kod[-1] == "4":
                czy_zero = False
                for cyfra in kod:
                    if cyfra == "0":
                        czy_zero = True
                        break
                if not czy_zero:
                    cnt += 1
        print(cnt, file=output_file)


def kod_to_dec(kod):
    return int(kod[:-1], int(kod[-1]))


# print(kod_to_dec("114"))
# print(kod_to_dec("119"))

def zadanie_6_3(data):
    with open("wyniki_6_3.txt", "w") as output_file:
        cnt = 0
        for kod in data:
            if kod[-1] == "2":
                if kod_to_dec(kod) % 2 == 0:
                    cnt += 1
        print(cnt, file=output_file)


def zadanie_6_4(data):
    with open("wyniki_6_4.txt", "w") as output_file:
        suma = 0
        for kod in data:
            if kod[-1] == "8":
                suma += kod_to_dec(kod)
        print(suma, file=output_file)


def zadanie_6_5(data):
    with open("wyniki_6_5.txt", "w") as output_file:
        min_kod = data[0]
        min_value_kod = kod_to_dec(data[0])
        max_kod = data[0]
        max_value_kod = kod_to_dec(data[0])
        for kod in data:
            kod_dec = kod_to_dec(kod)

            if kod_dec > max_value_kod:
                max_value_kod = kod_dec
                max_kod = kod

            if kod_dec < min_value_kod:
                min_value_kod = kod_dec
                min_kod = kod
        print(f"Kod najwiekszej {max_kod}, dec --- {max_value_kod}", file=output_file)
        print(f"Kod najmniejszej {min_kod}, dec --- {min_value_kod}", file=output_file)


def main():
    with open("liczby.txt", "r") as file:
        data = file.read().split("\n")
        zadanie_6_1(data)
        zadanie_6_2(data)
        zadanie_6_3(data)
        zadanie_6_4(data)
        zadanie_6_5(data)

main()
