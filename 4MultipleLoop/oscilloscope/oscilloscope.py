def input():
    return raw_input()


def layout():
    row = []
    for i in range(21):
        row.append([])
    for i in range(21):
        for j in range(60):
            row[i].append([''])
    return row


def oscilloscope(n, row):
    pass


def output(n, row):
    for i in range(21):
        output_row = ''
        for j in range(60):
            output_row += str(row[i][j])
        print output_row, '\n'


def main():
    #n = int(input())
    n = 5
    row = layout()
    oscilloscope(n, row)
    #test(n, row)
    output(n, row)


def test(n, row):
    for i in range(20):
        print 'row[i]', row[i]


main()


