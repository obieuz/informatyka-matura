from collections import Counter


def zadanie_6_1(dane):
    with open("wyniki6.txt", "w") as output_file:
        print("6.1", file=output_file)
        cnt = 0
        for rekord_slow in dane:
            slowa = rekord_slow.split(" ")
            if slowa[0][-1] == "A":
                cnt += 1
            if slowa[1][-1] == "A":
                cnt += 1
        print(cnt, file=output_file)


def zadanie_6_2(dane):
    with open("wyniki6.txt", "a") as output_file:
        print("6.2", file=output_file)
        cnt = 0
        for rekord_slow in dane:
            slowa = rekord_slow.split(" ")
            if slowa[0] in slowa[1]:
                cnt += 1
        print(cnt, file=output_file)


def zadanie_6_3(dane):
    with open("wyniki6.txt", "a") as output_file:
        print("6.3", file=output_file)
        cnt = 0
        tablica_rekordow = []
        for rekord_slow in dane:
            slowa = rekord_slow.split(" ")
            slowo1_litery = Counter(slowa[0])
            slowo2_litery = Counter(slowa[1])

            if slowo1_litery == slowo2_litery:
                tablica_rekordow.append((slowa[0],slowa[1]))
                cnt += 1
        print(f"Jest {cnt} takich wierszy", file=output_file)
        for rekord_wynikowy in tablica_rekordow:
            slowo1,slowo2 = rekord_wynikowy
            print(slowo1,slowo2, sep=" ", file=output_file)

def main():
    with open("slowa.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_6_1(dane)
        zadanie_6_2(dane)
        zadanie_6_3(dane)


main()
