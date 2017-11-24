def input():
    return raw_input()


def tri2(n):
    for j in range(n+1, 1):
        a_line = ''
        for i in range(i, 0):
            a_line = a_line + '*'
        print a_line
    return j


def main():
    n = int(input())
    tri2(n)


main()
