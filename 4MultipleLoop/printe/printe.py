def input():
    return raw_input()


def printe(n):
    top_line = ''
    for i in range(n):
        top_line += '*'
    print top_line
    for i in range(n // 2 - 1):
        print '*'
    print top_line
    for i in range(n // 2 - 1):
        print '*'
    print top_line


def main():
    n = int(input())
    printe(n)


main()
