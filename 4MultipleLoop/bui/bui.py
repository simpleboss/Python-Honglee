def input():
    return int(raw_input())


def print_top_line(n):
    top_line = ' **'
    for i in range(n):
        top_line += ' '
    top_line += '**'
    print top_line


def print_space_even(n):
    # up_line
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
    # down_line
    for j in range(3):
        down_line = ''
        for i in range(n//2 + j):
            down_line += ' '
        down_line += '*'
        for i in range(4 - 2 * j):
            down_line += ' '
        down_line += '*'
        print down_line


def print_space_odd(n):
    # up_line
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
    # three_star_line
    three_star_line = ''
    for i in range(n-2):
        three_star_line += ' '
    three_star_line += '*'
    print three_star_line
    # down_line
    for j in range(2):
        down_line = ''
        for i in range(n // 2 + 1 + j):
            down_line += ' '
        down_line += '*'
        for i in range(3 - 2 * j):
            down_line += ' '
        down_line += '*'
        print down_line


def main():
    # n = input()
    n = 3
    print_top_line(n)
    if n % 2 == 0:
        print_space_even(n)
    else:
        print_space_odd(n)

if __name__ == '__main__':
    main()
