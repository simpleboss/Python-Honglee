def input():
    return raw_input()


def etnirp(n):
    long_line = ''
    space_line = ''
    for i in range(n):
        long_line += '*'
    for i in range(n-1):
        space_line += ' '
    space_line += '*'
    print long_line
    for i in range(n // 2 - 1):
        print space_line
    print long_line
    for i in range(n // 2 - 1):
        print space_line
    print long_line


def main():
    n = int(input())
    etnirp(n)


main()
