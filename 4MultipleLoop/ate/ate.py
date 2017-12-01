def input():
    return int(raw_input())


def ate(n):
    answer = 0
    for i in range(100):
        for j in range(100):
            if n - i - j == 0:
                answer += 1
                # print 'i', i
                # print 'j', j
    print answer


def main():
    n = input()
    ate(n)


main()
