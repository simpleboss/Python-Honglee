def input():
    return raw_input()


def diamond(n):
    for i in range(n - 1):
        a_line = ''
        for j in range(n - 1 - i):
            a_line += ' '
        for j in range(2 * i + 1):
            a_line += '*'
        print a_line
    a_line = ''
    for i in range(2 * n - 1):
        a_line += '*'
    print a_line
    for i in range(n - 1):
        a_line = ''
        for j in range(i + 1):
            a_line += ' '
        for j in range(2 * (n - i - 1) - 1):
            a_line += '*'
        print a_line


def main():
    n = int(input())
    diamond(n)


main()
