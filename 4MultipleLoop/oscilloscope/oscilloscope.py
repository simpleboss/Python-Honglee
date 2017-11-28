def input():
    return raw_input()


def layout():
    row = []
    for i in range(21):
        for j in range(60):
            row.append([[' ']])
    return row


def oscilloscope(n, row):
    pass


def output(n, row):
    for i in range(21):
        for j in range(60):
            print row[i][j]
            print '\n'


def main():
    n = int(input())
    row = layout()
    oscilloscope(n, row)
    output(n, row)


main()
