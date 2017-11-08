def cha(num1, num2):
    print num1, num2,
    while num1 - num2 >= 0:
        num3 = num1 - num2
        print num3,
        num1 = num2
        num2 = num3
    return num1


num = []
num = [int(i) for i in raw_input().split(' ')]
num1 = num[0]
num2 = num[1]
cha(num1, num2)
