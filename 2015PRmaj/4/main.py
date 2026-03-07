from collections import Counter


def zadanie_4_1(liczby):
    with open("wyniki4.txt", "w") as output_file:
        print("4.1", file=output_file)
        cnt = 0
        for liczba in liczby:
            liczba_cyfr = Counter(liczba)
            if liczba_cyfr["0"] > liczba_cyfr["1"]:
                cnt += 1
        print(cnt, file=output_file)


def zadanie_4_2(liczby):
    with open("wyniki4.txt", "a") as output_file:
        print("4.2", file=output_file)
        cnt_2 = 0
        cnt_8 = 0
        for liczba in liczby:
            liczba = int(liczba,2)
            if liczba % 2 == 0:
                cnt_2 += 1
            if liczba % 8 == 0:
                cnt_8 += 1
        print(f"Podzielne przez 2 --- {cnt_2}", file=output_file)
        print(f"Podzielne przez 8 --- {cnt_8}", file=output_file)

def zadanie_4_3(liczby):
    with open("wyniki4.txt", "a") as output_file:
        print("4.3", file=output_file)
        min_value = int(liczby[0],2)
        max_value = int(liczby[0],2)
        min_index = 1
        max_index = 1
        for index,liczba in enumerate(liczby):
            liczba = int(liczba,2)

            if liczba > max_value:
                max_value = liczba
                max_index = index + 1

            if liczba < min_value:
                min_value = liczba
                min_index = index + 1

        print(min_index,max_index, sep=", ",file=output_file)

def main():
    # mock_data_1 = ["101011010011001100111","10001001","1000000","101010011100","100010"]
    # mock_data_2 = ["101011010011001100000","10001001","100100","101010010101011011000","100011"]
    # mock_data_3 = ["101011010011001100111","10001001011101010","1001000","101010011100","1000110"]
    with open("liczby.txt", "r") as file:
        liczby = file.read().split("\n")
        zadanie_4_1(liczby)
        zadanie_4_2(liczby)
        zadanie_4_3(liczby)
        # print(liczby)


main()
