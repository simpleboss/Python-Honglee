def input():
    return int(raw_input())


def answer(n):
    for i in range(0, n + 1, 1):
        a_line = ''
        for j in range(n, i, -1):
            a_line += str(j - i)
        print a_line


def main():
    n = input()
    answer(n)


#if __name__ == '___main___':
main()
