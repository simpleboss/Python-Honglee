def input():
    input_list = []
    input_list = [int(i) for i in raw_input().split(' ')]
    return input_list


def grp(n, k):
    print n
    print k


def main():
    input_list = input()
    n = input_list[0]
    k = input_list[1]
    grp(n, k)


main()
