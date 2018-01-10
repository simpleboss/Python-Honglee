def input():
    return int(raw_input())


def main(input_v):
    def make_row(input_v):
        row = []
        for i in range(2 * input_v + 1):
            row.append([])
        return row

    def stair_star(row, input_v):
        for i in range(len(row)):
            for j in range(i):
                row[i] += ' '
            row[i] += '*'
        return row

    def space_between_stars(row, input_v):
        for i in range(len(row)):
            for j in range(2 * input_v - i):
                row[i] += ' '
            row[i] += '*'
        return row

    row = make_row(input_v)
    stair_star(row, input_v)
    space_between_stars(row, input_v)

    for i in range(len(row) - 1, -1, -1):
        print("".join(str(x) for x in row[i]))


input_v = 5
main(input_v)
