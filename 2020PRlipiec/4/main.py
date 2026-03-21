def licz_sume(id):
    liczby = id[3:]
    suma = 0
    for liczba in liczby:
        suma += int(liczba)
    return suma


def zadanie_4_1(data):
    with open("wyniki4_1.txt", "w") as output_file:
        values = dict()
        for row in data:
            value = licz_sume(row)
            if value not in values:
                values[value] = [row]
            else:
                values[value].append(row)
        for ids in values.get(max(values)):
            print(ids, file=output_file)


def czy_palindrom(ciag_str):
    i = 0
    j = -1

    while i < len(ciag_str) // 2:
        if ciag_str[i] != ciag_str[j]:
            return False
        i += 1
        j -= 1
    return True


# print(czy_palindrom("KOK"))
# print(czy_palindrom("ABB"))

def zadanie_4_2(data):
    with open("wyniki4_2.txt", "w") as output_file:
        for row in data:
            if czy_palindrom(row[:3]) or czy_palindrom(row[3:]):
                print(row, file=output_file)


def suma_id(ids):
    suma = 0
    weights = [7, 3, 1]
    for i in range(len(ids)):
        # if ids[i].isascii()
        if ids[i].isdigit():
            suma += int(ids[i]) * weights[i % 3]
        else:
            suma += (ord(ids[i]) - 55) * weights[i % 3]
    return suma


# print("A".isdigit())
# print("1".isdigit())
# print(ord("A")-55)

def czy_poprawne(ids: str):
    control_digit = int(ids[3])
    ids = ids[:3] + ids[4:]

    if control_digit == suma_id(ids) % 10:
        return True
    return False

# print(czy_poprawne("CIS459437"))

def zadanie_4_3(data):
    with open("wyniki4_3.txt", "w") as output_file:
        for row in data:
            if not czy_poprawne(row):
                print(row, file=output_file)


def main():
    with open("identyfikator.txt", "r") as file:
        data = file.read().split("\n")[:-1]
        # print(data)
        zadanie_4_1(data)
        zadanie_4_2(data)
        zadanie_4_3(data)


main()
