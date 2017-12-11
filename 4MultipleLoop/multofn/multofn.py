def input():
    return int(raw_input())


def multofn(n):
    nominate_list = []
    answer = 0
    for i in range(1111, 3333):
        if i % n == 0:
            nominate_list.append(i)
    j_nb = []
    for j in range(len(nominate_list)):
        j_nb.append([])
        j_nb[j].append(j // 1000)
        j_nb[j].append(j // 100 - j_nb[j][0] * 10)
        j_nb[j].append(j // 10 - j_nb[j][1] * 100 - j_nb[j][0] * 1000)
        j_nb[j].append(j - j_nb[j][2] * 1000 - j_nb[j][1] * 100 - j_nb[j][0] * 1000)
    for j in range(len(j_nb)):
        for nb in j_nb[j]:
            nb123 = 1
            while nb123 < 4:
                if j_nb[j][int(nb)] == nb123:
                    j_nb[j].append('ok')
                    break
                nb123 += 1
    answer_count = 0
    for j in j_nb:
        answer = -1
        while answer > -5:
            if j_nb[j][answer] != 'ok':
                break
            answer -= 1
        if answer == -5:
            answer_count += 1
    print answer_count


def main():
    n = input()
    multofn(n)


main()
