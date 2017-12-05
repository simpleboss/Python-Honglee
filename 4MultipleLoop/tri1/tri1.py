def input():
    return raw_input()


def tri1(n):
    for i in range(0, n + 1):
        a_line = ''
        for j in range(0, i):
            a_line = a_line + '*'
            print 'j =', j
        print a_line
    return j


def main():
    n = int(input())
    tri1(n)


main()
