from math import log


def zadanie_4_1(dane):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        cnt = 0
        for liczba in dane:
            liczba = int(liczba)
            if log(liczba, 3) == int(log(liczba, 3)):
                cnt += 1
        print(cnt, file=output_file)


def oblicz_silnie(liczba):
    wynik = 1
    while liczba > 0:
        wynik *= liczba
        liczba -= 1
    return wynik


VALUES = {"0": 1, "1": 1, "2": 2, "3": 6, "4": 24, "5": 120, "6": 720, "7": 5040, "8": 40320, "9": 362880}


def oblicz_silnie_cyfr(liczba: str):
    wynik = 0
    for cyfra in liczba:
        wynik += VALUES[cyfra]
    return wynik

# print(oblicz_silnie_cyfr("145"))


# print(oblicz_silnie(6))
# print(oblicz_silnie(7))
# print(oblicz_silnie(8))
# print(oblicz_silnie(9))

def zadanie_4_2(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        for liczba in dane:
            if int(liczba) == oblicz_silnie_cyfr(liczba):
                print(liczba,file=output_file)

def NWD(a,b):
    a = int(a)
    b = int(b)
    while b!= 0:
        liczba = b
        b = a%b
        a = liczba
    return a

# print(NWD(70,28))

def zadanie_4_3(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        najd_ciag = 0
        najd_pocz_ciag = ""
        dzielnik_najd = 0
        curr_ciag = 2
        pocz_ciag = dane[0]
        dzielnik = NWD(dane[0],dane[1])

        for i in range(2,len(dane)-1):
            nwd = NWD(dzielnik,dane[i])

            if nwd == dzielnik and nwd != 1:
                curr_ciag += 1
                continue

            if curr_ciag > najd_ciag:
                najd_ciag = curr_ciag
                najd_pocz_ciag = pocz_ciag
                dzielnik_najd = dzielnik

            curr_ciag = 1
            pocz_ciag = dane[i]
            dzielnik = NWD(dane[i],dane[i+1])



        print(najd_pocz_ciag,najd_ciag,dzielnik_najd,file=output_file)





def main():
    with open("liczby.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
main()
