def input():
    return int(raw_input())


def multofn(n):
    nominate_list = []
    answer = 0
    for i in range(1111, 3333):
        if i % n == 0:
            nominate_list.append(i)
    for j in nominate_list:
        j_4 = j // 1000
        j_3 = j // 100 - j_4 * 10
        j_2 = j // 10 - j_4 * 100 - j_3 * 100
        j_1 = j - j_4 * 1000 - j_3 * 100 - j_2 * 10
        nb = 1
        while nb < 4:
            if j_4 != nb and j_3 != nb and j_2 != nb and j_1 != nb:
                break
            nb += 1
            print nominate_list[j]
        if nb == 4:            answer += 1
    print answer


def main():
    n = input()
    multofn(n)


main()
