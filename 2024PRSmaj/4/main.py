def stworz_plansze(dane):
    plansza = []
    dane = dane.split("\n")[:-1]
    for row in dane:
        plansza.append(row.split(" "))
    return plansza


def szukaj_sasiada(pos, plansza):
    x, y = pos

    statki = []
    puste_miejsca = []
    for i in range(y - 1, y + 2):
        if i < 0 or i >= len(plansza):
            continue
        for j in range(x - 1, x + 2):
            if i == y and j == x:
                continue
            if j < 0 or j >= len(plansza[i]):
                continue
            if plansza[i][j] == "1":
                statki.append((j, i))
            else:
                puste_miejsca.append((j, i))
    return statki, puste_miejsca

def zadanie_4_1(plansza):
    with open("wyniki4.txt","w") as output_file:
        print("4.1",file=output_file)
        cnt = 0
        for i in range(len(plansza)):
            for j in range(len(plansza[i])):
                if plansza[i][j] == "1":
                    continue
                else:
                    statki, wolne_miejsca = szukaj_sasiada((j,i),plansza)
                    if len(statki) == 0:
                        cnt +=1
        print(cnt,file=output_file)

def zadanie_4_2(plansza):
    with open("wyniki4.txt","a") as output_file:
        print("4.2",file=output_file)
        cnt = 0
        for i in range(1,len(plansza)):
            for j in range(0,i+1):
                if i == j:
                    continue

                if plansza[i][j] == plansza[j][i] and plansza[i][j]=="1":
                    statki_1, wolne_1 = szukaj_sasiada((j,i),plansza)

                    if len(statki_1) > 0:
                        continue

                    statki_2, wolne_2 = szukaj_sasiada((i,j),plansza)

                    if len(statki_2) > 0:
                        continue

                    cnt += 1
                    # print((i,j), (j,i), sep=" - ")

        print(cnt,file=output_file)

def zadanie_4_3(plansza):
    with open("wyniki4.txt","a") as output_file:
        print("4.3",file=output_file)
        cnt = 0
        for i in range(len(plansza)):
            for j in range(len(plansza[i])):
                if plansza[i][j] != "1":
                    continue
                statki, puste_miejsca = szukaj_sasiada((j,i), plansza)
                if len(statki) > 0:
                    cnt+=1

        # wiem ze licze podwojnie
        print(cnt//2,file=output_file)

def zadanie_4_4(plansza):
    with open("wyniki4.txt","a") as output_file:
        print("4.4",file=output_file)
        cnt_jedno = 0
        cnt_dwu = 0
        znalezione_statki = []
        for i in range(len(plansza)):
            if plansza[i][i] == "1":
                statki_obok, puste = szukaj_sasiada((i,i),plansza)
                if len(statki_obok) > 0:
                    cnt_dwu += 1
                else:
                    cnt_jedno +=1
                znalezione_statki.append((i, i))
                for statek in statki_obok:
                    znalezione_statki.append(statek)

        row_index = 0
        for i in range(len(plansza)-1,-1,-1):
            if plansza[row_index][i] == "1":
                if (i,row_index) in znalezione_statki:
                    row_index+=1
                    continue
                statki_obok, puste = szukaj_sasiada((i,row_index),plansza)
                if len(statki_obok) > 0:
                    cnt_dwu += 1
                else:
                    cnt_jedno +=1
            row_index+=1



        print(cnt_jedno,cnt_dwu,sep="\n",file=output_file)



def main():
    with open("plansza_przyklad.txt", "r") as file:
        plansza = stworz_plansze(file.read())
        zadanie_4_1(plansza)
        zadanie_4_2(plansza)
        zadanie_4_3(plansza)
        zadanie_4_4(plansza)

main()
