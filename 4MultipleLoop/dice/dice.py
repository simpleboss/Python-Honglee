def input():
    return int(raw_input())


def dice(n):
    answer = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                answer.append([i, j])
    i = 0
    while i < len(answer):
        j = 0
        while j < 2:
            print answer[i][j],
            j += 1
        print ''
        i += 1


def main(n):
    dice(n)

'''
if __name__ == '__main__':
    n = input()
    main(n)
'''
n = input()
main(n)
