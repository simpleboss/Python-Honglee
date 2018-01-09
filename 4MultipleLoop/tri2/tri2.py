def input():
    return raw_input()


def tri2(n):
    for j in range(n, 0, -1):
        a_line = ''
        for i in range(j - 1, -1, -1):
            a_line = a_line + '*'
            #print 'i =', i
        print a_line


def main():
    n = int(input())
    tri2(n)


main()
