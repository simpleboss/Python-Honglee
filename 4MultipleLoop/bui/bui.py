def input():
    return raw_input()


def print_top_line(n):
    top_line = ' **'
    for i in range(n):
        top_line += ' '
    top_line += '**'
    print top_line


def print_space_even(n):
    for up_space in range(n // 2):
        up_line = ''
        for i in range(up_space):
            up_line += ' '
        up_line += '*  *'
        if up_space <= n // 2 + 2:
            for i in range(n - 2 - 2 * up_space):
                up_line += ' '
            up_line += '*  *'
        print up_line
    for j in range(3):
        down_line = ''
        for i in range(n//2 + j):
            down_line += ' '
        down_line += '*'
        for i in range(5 - j):
            down_line += ' '
        down_line += '*'
        print down_line


def print_space_odd(n):
    pass


def main():
    #n = int(input())
    n = 20
    print_top_line(n)
    if n % 2 == 0:
        print_space_even(n)
    else:
        print_space_odd(n)


main()
