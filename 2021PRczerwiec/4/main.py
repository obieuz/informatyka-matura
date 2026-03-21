def zadanie_4_1(data):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        cnt = 0
        for row in data:
            for character in row:
                if character.isdigit():
                    cnt += 1
        print(cnt, file=output_file)


def zadanie_4_2(data):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        password = ""
        letter_index = 0
        for i in range(19, len(data), 20):
            password = password + data[i][letter_index]
            letter_index += 1

        print(password, file=output_file)


def czy_palindrom(tekst):
    i = 0
    j = -1
    while i < len(tekst) // 2:
        if tekst[i] != tekst[j]:
            return False
        i += 1
        j -= 1
    return True


def czy_prawie_palindrom(tekst):
    if czy_palindrom(tekst[1:]):
        return True, tekst[1:]
    elif czy_palindrom(tekst[:-1]):
        return True, tekst[:-1]
    return False, tekst


def zadanie_4_3(data):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        password = ""
        for word in data:
            result, final_word = czy_prawie_palindrom(word)
            if result:
                password = password + final_word[len(final_word) // 2]

        print(password, file=output_file)

def grupuj_liczby(word):
    digits_str = ""
    digits = []
    for character in word:
        if character.isdigit():
            digits_str = digits_str + character

    if len(digits_str) % 2 != 0:
        digits_str = digits_str[:-1]

    for i in range(0,len(digits_str),2):
        digits.append(int(digits_str[i]+digits_str[i+1]))
    return digits


def generuj_haslo(data):
    password = ""
    for word in data:
        digits = grupuj_liczby(word)

        for digit in digits:
            if 65 <= digit <= 90:
                password = password + chr(digit)

            if password[-3:len(password)] == "XXX":
                return password
    return password


def zadanie_4_4(data):
    with open("wyniki4.txt", "a") as output_file:
        print("4.4", file=output_file)
        password = generuj_haslo(data)
        print(password, file=output_file)


def main():
    with open("napisy.txt", "r") as file:
        data = file.read().split("\n")[:-1]
        zadanie_4_1(data)
        zadanie_4_2(data)
        zadanie_4_3(data)
        zadanie_4_4(data)

main()
