def get_values(row):
    splitted_row = row.split(" ")
    return int(splitted_row[0]), int(splitted_row[1])


def zadanie_3_1(data):
    with open("zadanie3_1.txt", "w") as output_file:
        lengths = set()
        for row in data:
            a, b = get_values(row)
            lengths.add(b - a + 1)
        lengths = sorted(lengths)
        print(lengths[0], file=output_file)
        print(lengths[1], file=output_file)


def zadanie_3_2(data):
    with open("zadanie3_2.txt", "w") as output_file:
        lengths = dict()
        for row in data:
            a, b = get_values(row)
            length = b - a + 1
            if length not in lengths:
                lengths[length] = 1
            else:
                lengths[length] += 1
        most_common = max(lengths.values())
        max_len = 0
        for key, value in lengths.items():
            if value == most_common:
                if key > max_len:
                    max_len = key
        print(max_len, file=output_file)


class Row:
    def __init__(self, a, b, row):
        self.a = a
        self.b = b
        self.row = row
        self.dl = b - a + 1

    def __str__(self):
        return f"{self.row, self.dl}"


def zadanie_3_3(data):
    with open("zadanie3_3.txt", "w") as output_file:
        rows = []
        lengths = dict()
        for row in data:
            a, b = get_values(row)
            row = Row(a, b, row)
            rows.append(row)
            lengths[row.row] = 1
        rows.sort(key=lambda row: row.dl)

        for i in range(len(rows) - 1):
            for j in range(i + 1, len(rows)):

                if rows[i].a >= rows[j].a and rows[i].b <= rows[j].b:

                    if lengths[rows[j].row] < lengths[rows[i].row] + 1:
                        lengths[rows[j].row] = lengths[rows[i].row] + 1
        print(max(lengths.values()),file=output_file)


# zadanie_3_3(["-2 4", "-4 3", "-3 6","-1 2","0 3","1 1", "7 9"])


def main():
    with open("dane3.txt", "r") as file:
        data = file.read().split("\n")[:-1]
        # print(data)
        zadanie_3_1(data)
        zadanie_3_2(data)
        zadanie_3_3(data)


main()
