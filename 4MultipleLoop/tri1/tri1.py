def input():
    return raw_input()


def tri1(n):
    import sys
    for i in range(0, n + 1):
        for j in range(0, i):
            sys.stdout.write('*')
        print ''
    return j


def main():
    n = int(input())
    tri1(n)

main()