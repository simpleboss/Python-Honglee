def input():
    return int(raw_input())


def ddiamond(n):
    a_line = []
    for i in range(n // 2 + 1):
        a_line.append([])
        for j in range((n // 2) - i, 0, -1):
            a_line[i] += ' '
        for j in range(i+1):
            a_line[i] += str(j+1)
        for j in range(i+1, 1, -1):
            a_line[i] += str(j-1)
        print ''.join(a_line[i])
    for i in range(n // 2 -1, -1, -1):
        print ''.join(a_line[i])

def main():
    n = input()
    #n = 11
    ddiamond(n)


main()
