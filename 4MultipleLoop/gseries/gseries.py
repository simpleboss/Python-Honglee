def input():
    return int(raw_input())


def gseries(n):
    total = 0
    for i in range(n):
        sum_n = 0
        for j in range(i+1):
            sum_n += j+1
        total += sum_n
    print total

def main():
    n = input()
    gseries(n)


main()
