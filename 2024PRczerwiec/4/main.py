from collections import Counter


def zadanie_4_1(dane):
    with open("wyniki4.txt","w") as output_file:
        print("4.1",file=output_file)
        cnt = 0
        for slowo in dane:
            if len(slowo)<3:
                continue
            for i in range(len(slowo)-2):
                if slowo[i] == "k" and slowo[i+2] == "t":
                    cnt += 1
                    break
        print(cnt,file=output_file)

def zadanie_4_2(dane):
    with open("wyniki4.txt","a") as output_file:
        print("4.2",file=output_file)
        for slowo in dane:
            if len(slowo)<5:
                continue
            for i in range(len(slowo)-4):
                if slowo[i] == "e" and slowo[i+4] == "e":
                    print(slowo[i:i+5],file=output_file)

def przeksztalc_na_rot13(slowo):
    key = 13
    output_string = ""
    for litera in slowo:
        ascii_litera = ord(litera) + key
        if ascii_litera > ord('z'):
            ascii_litera = ord('a') - 1 + (ascii_litera - ord('z'))
        output_string += chr(ascii_litera)
    return output_string

# print(przeksztalc_na_rot13("aren"))

def czy_odwrotnosc(slowo1,slowo2):
    i = 0
    j = -1
    while i < len(slowo1):
        if slowo1[i] != slowo2[j]:
            return False
        i += 1
        j -= 1
    return True

# print(czy_odwrotnosc("aren","nera"))
# print(czy_odwrotnosc("skibidi","toilet"))

def zadanie_4_3(dane):
    with open("wyniki4.txt","a") as output_file:
        print("4.3",file=output_file)
        cnt = 0
        max_length = 0
        max_length_word = ""
        for slowo in dane:
            slowo_rot13 = przeksztalc_na_rot13(slowo)

            if czy_odwrotnosc(slowo,slowo_rot13):
                cnt += 1

                if len(slowo) > max_length:
                    max_length = len(slowo)
                    max_length_word = slowo
        print(cnt,max_length_word,sep="\n",file=output_file)


def zadanie_4_4(dane):
    with open("wyniki4.txt", "a") as output_file:
        print("4.4", file=output_file)
        for slowo in dane:
            if len(slowo) < 2:
                print(slowo,file=output_file)
                continue

            liczba_liter = Counter(slowo)
            max_wyst = max(liczba_liter.values())

            if len(slowo) % 2 != 0:
                if max_wyst >= (len(slowo) + 1) // 2:
                    print(slowo, file=output_file)
            else:
                if max_wyst >= len(slowo) // 2:
                    print(slowo,file=output_file)


def main():
    with open("slowa.txt","r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
        zadanie_4_4(dane)
main()