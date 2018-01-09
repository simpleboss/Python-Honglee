def input():
    return int(raw_input())


def main(n):
    for space in range(0, n // 2 + 1):
        line = ''
        for i in range(space):
            line += ' '
        for i in range(n - 1 - (space * 2)):
            line += '*'
        line += '$'
        print line
    for space in range(n // 2 - 1, -1, -1):
        line = ''
        for i in range(space):
            line += ' '
        line += '$'
        for i in range(0, 2 * (n // 2 - space), 1):
            line += '*'
        print line


n = input()
main(n)
