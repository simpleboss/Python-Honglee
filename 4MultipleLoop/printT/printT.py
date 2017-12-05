def input():
    return raw_input()


def printt(n):
    long_line = ''
    for i in range(n):
        long_line += '*'
    print long_line
    one_star_line = ''
    for i in range(n // 2 ):
        one_star_line += ' '
    one_star_line += '*'
    for i in range(n-1):
        print one_star_line


def main():
    n = int(input())
    printt(n)


main()