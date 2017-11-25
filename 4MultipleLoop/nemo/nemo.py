def input():
    return raw_input()

def nemo(n):
    long_line = ''
    for i in range(n):
        long_line += '*'
    space_line = '*'
    for i in range(n - 2):
        space_line += ' '
    space_line += '*'
    print long_line
    for i in range(n - 2):
        print space_line
    print long_line


def main():
    n = int(input())

    nemo(n)


main()
