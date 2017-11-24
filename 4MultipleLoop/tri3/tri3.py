def input():
    return raw_input()


def tri3(n):
    result = []
    for j in range(1, n + 1):
        space_line = ''
        star_line = ''
        for i in range(1, j):
            space_line += ' '
        for i in range(n + 1 - j, 0, -1):
            star_line += '*'
        print space_line + star_line
    return j


def main():
    n = int(input())
    tri3(n)


main()