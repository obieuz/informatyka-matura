from collections import Counter
def czy_poprawny(ciag):
    counter = Counter(ciag)
    if counter["["] == counter["]"]:
        return True
    return False

def oblicz_glebokosc(ciag):
    max_pod_rzad = 0
    curr_rzad = 0
    for znak in ciag:
        if znak == "[":
            curr_rzad += 1
        else:
            if curr_rzad>max_pod_rzad:
                max_pod_rzad = curr_rzad
            if curr_rzad > 0:
                curr_rzad -= 1
            else:
                curr_rzad = 0
    return max_pod_rzad

# print(czy_poprawny("[ ] [ ]"))
# print(czy_poprawny("[ [ ] [ ] ] [ ] ]"))
# print(czy_poprawny("[ ] [ [ ] [ [ ] [ [ ] [ ] ] ] ]"))

print(oblicz_glebokosc("[]"))
print(oblicz_glebokosc("[][]"))
print(oblicz_glebokosc("[[][]]"))
print(oblicz_glebokosc("[[][[]]]"))
print(oblicz_glebokosc("[[[[][]][]]]"))

def zadanie_2_3():
    with open("dane2_3.txt","r") as file:
        dane = file.read().split("\n")[:-1]
        with open("zadanie2_3.txt","w") as output_file:
            for row in dane:
                print(oblicz_glebokosc(row),file=output_file)
zadanie_2_3()

def zadanie_2_4():
    with open("dane2_4.txt","r") as file:
        dane = file.read().split("\n")[:-1]
        with open("zadanie2_4.txt","w") as output_file:
            for row in dane:
                if czy_poprawny(row):
                    print("tak",file=output_file)
                else:
                    print("nie", file=output_file)
zadanie_2_4()
