def zadanie_a(napisy):
    with open("zadanie4.txt","w") as output_file:
        print("a",file=output_file)
        liczba_parzystych_napisow = 0
        for napis in napisy:
            if len(napis) % 2 != 0:
                continue
            liczba_parzystych_napisow +=1

        print(liczba_parzystych_napisow,file=output_file)

def zadanie_b(napisy):
    with open("zadanie4.txt","a") as output_file:
        print("b",file=output_file)
        liczba_napisow_z_taka_sama_iloscia = 0
        for napis in napisy:
            if len(napis) % 2 != 0:
                continue

            liczba_zer = 0
            liczba_jedynek = 0

            for index in range(len(napis)):
                if napis[index] == "0":
                    liczba_zer += 1
                    continue

                liczba_jedynek += 1

            if liczba_zer == liczba_jedynek:
                liczba_napisow_z_taka_sama_iloscia += 1

        print(liczba_napisow_z_taka_sama_iloscia,file=output_file)

def czy_tylko_z_znaku(slowo,znak):
    for i in range(len(slowo)):
        if slowo[i]!=znak:
            return False
    return True

def zadanie_c(napisy):
    with open("zadanie4.txt","a") as output_file:
        print("c",file=output_file)
        liczba_znakow_z_zer = 0
        liczba_znakow_z_jedynek = 0
        for napis in napisy:
            if czy_tylko_z_znaku(napis,"0"):
                liczba_znakow_z_zer +=1

            if czy_tylko_z_znaku(napis,"1"):
                liczba_znakow_z_jedynek +=1

        print(f"Z samych zer - {liczba_znakow_z_zer} \nZ samych jedynek - {liczba_znakow_z_jedynek}",file=output_file)

#zadanie_c(["000","111","010"])

def zadanie_d(napisy):
    with open("zadanie4.txt","a") as output_file:
        print("d",file=output_file)
        liczba_napisow_o_dlugosci_k = [0 for i in range(15)]

        for napis in napisy:
            dlugosc_napisu = len(napis)

            liczba_napisow_o_dlugosci_k[dlugosc_napisu-2]+=1

        for index,liczba in enumerate(liczba_napisow_o_dlugosci_k):
            print(f"Dla k={index+2} jest {liczba} liczb", file=output_file)

def main():
    with open("napisy.txt","r") as file:
        napisy = file.read().split("\n")[:-1]


        zadanie_a(napisy)
        zadanie_b(napisy)
        zadanie_c(napisy)
        zadanie_d(napisy)

main()