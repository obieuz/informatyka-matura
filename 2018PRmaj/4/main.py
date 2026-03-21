
def zadanie_4_1(slowa):
    with open("wyniki4.txt" ,"w") as output_file:
        print("4.1" ,file=output_file)
        slowo_finalne = ""
        for i in range(39, len(slowa), 40):
            slowo_finalne = slowo_finalne + slowa[i][9]
        print(slowo_finalne ,file=output_file)

def zadanie_4_2(slowa):
    with open("wyniki4.txt" ,"a") as output_file:
        print("4.2" ,file=output_file)
        slowo_max = slowa[0]
        liczba_max = len(set(slowo_max))
        for slowo in slowa:
            liczba = len(set(slowo))

            if liczba > liczba_max:
                liczba_max = liczba
                slowo_max = slowo

        print(slowo_max, liczba_max,file=output_file)

def czy_4_3_warunek(slowo):
    for i in range(len(slowo)-1):
        if abs(ord(slowo[i]) - ord(slowo[i+1])) > 10:
            return False
    return True

# print(czy_4_3_warunek("CGECF"))
# print(czy_4_3_warunek("ABEZA"))
def zadanie_4_3(slowa):
    with open("wyniki4.txt" ,"a") as output_file:
        print("4.3" ,file=output_file)

        for slowo in slowa:
            if czy_4_3_warunek(slowo):
                print(slowo,file=output_file)

# print(abs(ord('A')-ord('B')))

def main():
    with open("sygnaly.txt" ,"r") as file:
        dane = file.read().split("\n")[:-1]
        # print(dane)
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
main()
