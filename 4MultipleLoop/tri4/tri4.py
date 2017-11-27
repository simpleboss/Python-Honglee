def input():
    return raw_input()


def tri4(n):
    for i in range(n // 2 + 1):
        a_line = ''
        for j in range(n // 2 - i):
            a_line += ' '
        for j in range(2 * i + 1):
            a_line += '*'
        print a_line


def main():
    n = int(input())
    tri4(n)


main()
