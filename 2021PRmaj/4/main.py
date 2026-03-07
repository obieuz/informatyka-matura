def przesun_litere(litera) -> str:
    ascii_litera = ord(litera) + 1
    if ascii_litera > ord('Z'):
        ascii_litera = ord('A') - 1 + (ascii_litera - ord('Z'))
    return chr(ascii_litera)


def handle_commands(command,arg,tekst):
    if command == "DOPISZ":
        tekst = tekst + arg
    elif command == "USUN":
        tekst = tekst[:-1]
    elif command == "ZMIEN":
        tekst = tekst[:-1] + arg
    elif command == "PRZESUN":
        for index in range(len(tekst)):
            if tekst[index]==arg:
                tekst = tekst[:index] + przesun_litere(arg) + tekst[index+1:]
                break
    return tekst

def rozklad_komend(row):
    dane = row.split(" ")
    return dane[0], dane[1]


def transormuj(dane):
    output_string = ""
    for row in dane:
        command, arg = rozklad_komend(row)

        output_string = handle_commands(command,arg,output_string)
    return output_string

def zadanie_4_1(dane):
    with open("wyniki4.txt","w") as output_file:
        print("4.1",file=output_file)

        final_string = transormuj(dane)

        print(len(final_string),file=output_file)

def zadanie_4_2(dane):
    with open("wyniki4.txt","a") as output_file:
        print("4.2",file=output_file)

        max_commend = ""
        current_commend = ""
        max_commend_cnt = 1
        current_commend_cnt = 1
        for row in dane:
            command, arg = rozklad_komend(row)
            if command == current_commend:
                current_commend_cnt += 1
            if current_commend != command:
                current_commend = command
                current_commend_cnt = 1
            if current_commend_cnt > max_commend_cnt:
                max_commend_cnt = current_commend_cnt
                max_commend = current_commend
        print(f"{max_commend} {max_commend_cnt}",file=output_file)

def zadanie_4_3(dane):
    with open("wyniki4.txt","a") as output_file:
        print("4.3",file=output_file)

        arg_directory = dict()
        for row in dane:
            command, arg = rozklad_komend(row)
            if command != "DOPISZ":
                continue

            if arg not in arg_directory:
                arg_directory[arg] = 1
            else:
                arg_directory[arg] += 1

        print(f"{max(arg_directory, key=arg_directory.get)} {max(arg_directory.values())}",file=output_file)

def zadanie_4_4(dane):
    with open("wyniki4.txt","a") as output_file:
        print("4.4",file=output_file)

        final_string = transormuj(dane)

        print(final_string,file=output_file)
def main():
    with open("instrukcje.txt","r") as file:
        dane = file.read().split("\n")[:-1]
        zadanie_4_1(dane)
        zadanie_4_2(dane)
        zadanie_4_3(dane)
        zadanie_4_4(dane)

main()