def input():
    return raw_input()


def printh(n):
    long_line = ''
    for i in range(n):
        long_line += '*'
    two_star_line = '*'
    for i in range(n - 2):
        two_star_line += ' '
    two_star_line += '*'
    for i in range((n - 1) / 2):
        print two_star_line
    print long_line
    for i in range((n - 1) / 2):
        print two_star_line


def main():
    n = int(input())
    printh(n)


main()
