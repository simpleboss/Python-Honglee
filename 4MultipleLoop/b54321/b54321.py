def input():
    return int(raw_input())


def answer(n):
    i = 0
    while i <= n:
        a_line = ''
        for j in range(i):
            a_line += ' '
        for j in range(n, 0, -1):
            if j - i >= 1:
                a_line += str(j - i)
        print a_line
        i += 1


def main():
    n = input()
    answer(n)


#if __name__ == '___main___':
main()
