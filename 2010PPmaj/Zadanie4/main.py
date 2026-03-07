def czy_palindrom(slowo):
    for index in range((len(slowo) // 2)):
        if slowo[index] != slowo[-index-1]:
            return False
    return True


# print(czy_palindrom("JABFDFBAJ")) #True
# print(czy_palindrom("HAJAHAJAH")) #True
# print(czy_palindrom("ABBA")) #True
# print(czy_palindrom("JANA")) #False


def zadanie4(slowa):
    with open("zadanie4.txt", "w") as output_file:
        for slowo in slowa:
            if not czy_palindrom(slowo):
                continue

            print(slowo, file=output_file)


def main():
    with open("dane.txt", "r") as file:
        slowa = file.read().split("\n")

        zadanie4(slowa)


main()
