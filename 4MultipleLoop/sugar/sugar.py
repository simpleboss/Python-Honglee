def input():
    return int(raw_input())


def sugar(n):
    answer = []
    if n % 3 == 0:
        answer.append(n / 3)
    if n % 5 == 0:
        answer.append(n / 5)
    for i in range(n // 3):
        for j in range(n // 5):
            if (3 * (i + 1)) + (5 * (j + 1)) == n:
                answer.append(i + j + 2)
    for i in range(n // 5):
        for j in range(n // 3):
            if (5 * (i + 1)) + (3 * (j + 1)) == n:
                answer.append(i + j + 2)
    if answer == []:
        print '-1'
    else:
        print min(answer)


def main():
    n = input()
    sugar(n)


main()
