def input():
    return raw_input()


def sclock(n):
    for i in range(n // 2):
        a_line = ''
        for j in range(i):
            a_line += ' '
        for j in range(n - 1 - 2 * i):
            a_line += '*'
        a_line += '$'
        print a_line
    for i in range(n // 2 + 1):
        a_line = ''
        for j in range(n // 2 - i):
            a_line += ' '
        a_line += '$'
        for j in range(2 * i):
            a_line += '*'
        print a_line


def main():
    n = int(input())
    sclock(n)


main()
