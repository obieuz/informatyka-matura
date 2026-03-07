
def zadanie1(pesle):
    with open("wyniki6.txt","w", encoding="utf-8") as output_file:
        print("1", file=output_file)
        ile_kobiet = 0
        for pesel in pesle:
            if int(pesel[-2])%2==0:
                ile_kobiet+=1
        print(f"Jest {ile_kobiet} kobiet", file=output_file)
        print(f"Jest {len(pesle)-ile_kobiet} mężczyzn", file= output_file)

def zadanie2(pesle):
    with open("wyniki6.txt", "a", encoding="utf-8") as output_file:
        print("2", file=output_file)
        ile_osob_w_listopadzie = 0
        for pesel in pesle:
            miesiac = pesel[2]+pesel[3]
            if miesiac == "11" or miesiac == "31":
                ile_osob_w_listopadzie += 1
        print(f"Jest {ile_osob_w_listopadzie} urodzonych w listopadzie", file=output_file)

def sprawdz_pesel(pesel):
    wagi = [1,3,7,9,1,3,7,9,1,3]
    suma = 0
    for i in range(len(pesel)-1):
        suma += int(pesel[i])*wagi[i]
    suma += int(pesel[-1])
    if suma%10!=0:
        return False
    return True


def zadanie3(pesle):
    with open("wyniki6.txt", "a", encoding="utf-8") as output_file:
        print("3", file=output_file)
        for pesel in pesle:
            if sprawdz_pesel(pesel):
                continue
            print(pesel, file=output_file)
def main():
    with open("dane.txt","r") as file:
        pesle = file.read().split("\n")[:-1]

        zadanie1(pesle)
        zadanie2(pesle)
        zadanie3(pesle)

main()