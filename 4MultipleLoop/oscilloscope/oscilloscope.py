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
    pass


def output(row):
    i = 0
    while i < 11:
        print ''.join(row[i]),
        if i == 0:
            print '| 10V'
        else:
            print '|  ' + str(10 - i) + 'V'
        i += 1
    i = 12
    while i < 23:
        print ''.join(row[i]),
        print '| -' + str(i - 11) + 'V'
        i += 1


def main():
    #n = int(input())
    n = 5
    row = layout()
    oscilloscope(n, row)
    output(row)


main()
