LENGTH_OF_ALPHABET = 26

def szyfruj(word,key):
    output_word = ""
    key %= LENGTH_OF_ALPHABET
    for letter in word:
        output_letter = ord(letter) + key
        if output_letter > 90:
            output_letter = ord('A') + (output_letter - ord('Z') -1)
        output_word = output_word + chr(output_letter)
    return output_word

def odszyfruj(word,key):
    output_word = ""
    key %= LENGTH_OF_ALPHABET
    for letter in word:
        output_letter = ord(letter) - key
        if output_letter < 65:
            output_letter = ord('Z') - (ord('A') - output_letter -1)
        output_word = output_word + chr(output_letter)
    return output_word

# print(odszyfruj("BCYKUNCM",1718))

#zwraca True | False
def czy_dobrze_zaszyfrowane(word,zaszyfrowane):
    if ord(zaszyfrowane[0]) > ord(word[0]):
        key = ord(zaszyfrowane[0]) - ord(word[0])
    else:
        key = LENGTH_OF_ALPHABET - abs(ord(zaszyfrowane[0]) - ord(word[0]))
    if szyfruj(word,key) == zaszyfrowane:
        return True
    return False

# print(czy_dobrze_zaszyfrowane("DRAB","LZIJ"))

def zadanie6_1():
    with open("dane_6_1.txt","r") as file:
        words = file.read().split("\n")[:-1]
    with open("wyniki_6_1.txt","w") as output_file:
        for word in words:
            print(szyfruj(word,107),file=output_file)

def wyciagnij_slowo_klucz(line):
    values = line.split(" ")
    if values[1] == '':
        values[1] = 0
    return values[0],int(values[1])

# print(wyciagnij_slowo_klucz("BCYKUNCM 1718"))

def zadanie6_2():
    with open("dane_6_2.txt","r") as file:
        lines = file.read().split("\n")[:-1]
    with open("wyniki_6_2.txt","w") as output_file:
        for line in lines:
            word, key = wyciagnij_slowo_klucz(line)
            print(odszyfruj(word,key),file=output_file)

def wyciagnij_slowa(line):
    values = line.split(" ")
    if values[1] == '':
        values[1] = 0
    return values[0],values[1]

def zadanie6_3():
    with open("dane_6_3.txt","r") as file:
        lines = file.read().split("\n")[:-1]
    with open("wyniki_6_3.txt","w") as output_file:
        for line in lines:
            word, zaszyfrowane = wyciagnij_slowa(line)
            # case inna dlugosc
            if len(word) != len(zaszyfrowane):
                print(word,file=output_file)
            if czy_dobrze_zaszyfrowane(word, zaszyfrowane):
                continue
            print(word, file=output_file)




def main():
    zadanie6_1()
    zadanie6_2()
    zadanie6_3()
main()