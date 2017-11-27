def input():
    return raw_input()


def zorro(n):
    long_line = ''
    for i in range(n):
        long_line += '*'
    print long_line
    middle_line = ''
    for i in range(n-2):
        for j in range(n - 2 - i):
            middle_line += ' '
        middle_line += '*'
        for j in range(i + 1):
            middle_line += ' '
        print middle_line
        middle_line = ''
    print long_line

def main():
    n = int(input())
    zorro(n)


main()
