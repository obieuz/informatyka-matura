def czy_palindrom(symbol):
    i = 0
    j = -1
    while i < len(symbol) // 2:
        if symbol[i] != symbol[j]:
            return False
        i += 1
        j -= 1
    return True


def czy_prawie_palindrom(symbol):
    i = 0
    j = -1
    zmiany = 0
    while i < len(symbol) // 2:
        if symbol[i] != symbol[j]:
            zmiany += 1
            if zmiany > 1:
                return False
        i += 1
        j -= 1
    return True


# print(czy_prawie_palindrom("*+++++++++**"))
# print(czy_prawie_palindrom("*++++++++-+*"))
# print(czy_prawie_palindrom("*++-+++++-+*"))

def zadanie_4_1(symbole):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        for symbol in symbole:
            if czy_palindrom(symbol):
                print(symbol, file=output_file)


def zadanie_4_2(symbole):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        cnt = 0
        for symbol in symbole:
            if not czy_palindrom(symbol):
                if czy_prawie_palindrom(symbol):
                    cnt += 1
        print(cnt, file=output_file)


def czy_jest_kwadrat(pos, symbole):
    x, y = pos
    znak = symbole[y][x]
    for i in range(y, y + 3):
        for j in range(x, x + 2):
            if symbole[i][j] != symbole[i][j + 1] or symbole[i][j] != znak:
                return False
    return True


def zadanie_4_3(symbole):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        cnt = 0
        for i in range(len(symbole)-2):
            for j in range(len(symbole[i])-2):
                if czy_jest_kwadrat((j,i), symbole):
                    cnt += 1
                    print(f"Wiersz {i+2}, pole {j+2}",file=output_file)
        print(f"Liczba kwadratow - {cnt}",file=output_file)

def zamien_na_dec(symbol):
    values = {"o":"0","+":"1","*":"2"}
    trojkowy_string = ""
    for znak in symbol:
        trojkowy_string += values[znak]
    return int(trojkowy_string,3)

# print(zamien_na_dec("***+o*ooo++o"))


def zadanie_4_4(symbole):
    with open("wyniki4.txt", "a") as output_file:
        print("4.4", file=output_file)

        max_symbol = ""
        max_symbol_value = -1
        for symbol in symbole:
            dec_value = zamien_na_dec(symbol)

            if max_symbol_value < dec_value:
                max_symbol_value = dec_value
                max_symbol = symbol

        print(max_symbol_value, max_symbol, file=output_file)

def zamien_na_symbole(liczba):
    trojkowy_string = ""
    while liczba > 0:
        trojkowy_string = str(liczba%3) + trojkowy_string
        liczba //= 3
    values = {"0": "o", "1": "+", "2": "*"}
    symbol = ""
    for znak in trojkowy_string:
        symbol += values[znak]
    return symbol
# print(zamien_na_symbole(4841542))

def zadanie_4_5(symbole):
    with open("wyniki4.txt", "a") as output_file:
        print("4.5", file=output_file)
        suma = 0
        for symbol in symbole:
            suma += zamien_na_dec(symbol)

        print(suma, zamien_na_symbole(suma), file=output_file)

def main():
    with open("symbole.txt", "r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
        zadanie_4_4(dane)
        zadanie_4_5(dane)
main()
