def input():
    input_list = []
    input_list = [int(i) for i in raw_input().split(' ')]
    return input_list


def grp(n, k):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, i + k):
            sum += j
        if j <= n and sum % 15 == 0:
             answer += 1
    print answer


def main():
    input_list = input()
    n = input_list[0]
    k = input_list[1]
    grp(n, k)
    print 'test for pull request10'

main()
