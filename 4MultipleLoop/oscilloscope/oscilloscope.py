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
    # vertical line
    j = n
    while j <= 60:
        if j == n or (j - n) % (2 * n) == 0:
            i = 0
            #print 'j', j
            while i <= 2 * n:
                row[10 - n + i][j] = '*'
                i += 1
        j += 1

    # continuous wave
    j = n
    while j < 60:
        for k in range(2 * n):
            if j <= 59:
                row[10 + n - k][j] = '*'
                #print '10+n-k', 10+n-k
                #print 'j', j
                j += 1


def output(row):
    i = 0
    while i < 11:
        print ''.join(row[i]),
        if i == 0:
            print '| 10V'
        else:
            print '|  ' + str(10 - i) + 'V'
        i += 1
    i = 11
    while i < 21:
        print ''.join(row[i]),
        print '| -' + str(i - 10) + 'V'
        i += 1


def main():
    n = int(input())
    row = layout()
    oscilloscope(n, row)
    output(row)


main()
