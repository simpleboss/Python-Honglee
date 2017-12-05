def input():
    return raw_input()


def printf(n):
    long_line = ''
    for i in range(n):
        long_line += '*'
    print long_line
    for i in range(n // 2 - 1):
        print '*'
    print long_line
    for i in range(n // 2):
        print '*'


def main():
    n = int(input())
    printf(n)


main()
