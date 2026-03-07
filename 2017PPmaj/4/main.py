def dostan_cyfry_z_linii(linia):
    cyfry = linia.split(" ")
    cyfry = [int(cyfra) for cyfra in cyfry]
    return cyfry[0], cyfry[1], cyfry[2]


# print(dostan_cyfry_z_linii("20634 31423 261")) # (20634, 31423, 261)

def zadanie_1(linie):
    with open("wyniki4.txt", "w") as output_file:
        print("1", file=output_file)
        counter = 0
        for linia in linie:
            liczba1, liczba2, liczba3 = dostan_cyfry_z_linii(linia)

            if liczba1 > liczba2:
                continue

            if liczba2 > liczba3:
                continue

            counter += 1
        print(counter, file=output_file)


# zadanie_1(['20634 31423 261', '11009 21970 32126']) #1

def NWD(a, b):
    while b != 0:
        liczba = b
        b  = a % b
        a = liczba
    return a

# print(NWD(3,6)) # 3
# print(NWD(NWD(34,10),NWD(10,4))) #2


def zadanie_2(linie):
    with open("wyniki4.txt", "a") as output_file:
        print("2", file=output_file)
        suma = 0
        for linia in linie:
            liczba1, liczba2, liczba3 = dostan_cyfry_z_linii(linia)

            NWD_linii = NWD(NWD(liczba1,liczba2),NWD(liczba2,liczba3))
            suma += NWD_linii
        print(suma, file=output_file)

# zadanie_2(["3 6 9","34 10 4","36 20 28","16 40 56"]) #17


def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra
        liczba //= 10
    return suma

def zadanie_3(linie):
    with open("wyniki4.txt", "a", encoding="utf-8") as output_file:
        print("3", file=output_file)
        counter_rowne_35 = 0
        counter_max = 0
        max_suma_cyfr = 0
        czy_pierwsza_linia = True
        sumy_cyfr = []
        for linia in linie:
            liczba1, liczba2, liczba3 = dostan_cyfry_z_linii(linia)

            suma_cyfr_w_linii = suma_cyfr(liczba1) + suma_cyfr(liczba2) + suma_cyfr(liczba3)

            if czy_pierwsza_linia:
                max_suma_cyfr = suma_cyfr_w_linii
                czy_pierwsza_linia = False

            if max_suma_cyfr < suma_cyfr_w_linii:
                max_suma_cyfr = suma_cyfr_w_linii

            sumy_cyfr.append(suma_cyfr_w_linii)

            if suma_cyfr_w_linii != 35:
                continue

            counter_rowne_35 += 1

        for suma_linii in sumy_cyfr:
            if suma_linii != max_suma_cyfr:
                continue
            counter_max +=1

        print(f"Liczba liczb w których suma cyfr = 35 --- {counter_rowne_35}", file=output_file)
        print(f"Największa suma cyfr --- {max_suma_cyfr}", file=output_file)
        print(f"Liczba gdzie suma cyfr = {max_suma_cyfr} --- {counter_max}", file=output_file)


# zadanie_3(["45 9151 2800","2882 15040 2800","30172 2592 1102","29121 23564 320","3 243 765"]) # 2, 40, 2

def main():
    with open("liczby.txt", "r") as file:
        linie = file.read().split("\n")[:-1]

        zadanie_1(linie)
        zadanie_2(linie)
        zadanie_3(linie)

main()
