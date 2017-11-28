def input():
    return raw_input()


def layout():
    row = []
    for i in range(22):
        row.append([])
    for i in range(22):
        for j in range(60):
            row[i].append(' ')
    return row


def oscilloscope(n, row):
    # first wave
    column = 0
    while column <= n:
        row[10-column][column] = '*'
        column += 1
    i = 0
    while i <= 2 * n:
        row[10 - n + i][n] = '*'
        column += 1
        i += 1
    # continuous wave



def output(row):
    i = 0
    while i < 11:
        print ''.join(row[i]),
        if i == 0:
            print '| 10V'
        else:
            print str(i) + '|  ' + str(10 - i) + 'V'
        i += 1
    i = 12
    while i < 22:
        print ''.join(row[i]),
        print str(i) + '| -' + str(i - 11) + 'V'
        i += 1


def main():
    #n = int(input())
    n = 5
    row = layout()
    oscilloscope(n, row)
    output(row)


main()
