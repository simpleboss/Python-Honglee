def step(x, y):
    result = -1
    if x == 1 and y == 1:
        result = 1
    elif x == y:
        if x % 2 == 0:
            result = x * 2
        else:
            result = x * 2 + 1
    elif x % 2 == 0 and y % 2 == 0:
        result = x + y
    elif x % 2 != 0 and y % 2 != 0:
        result = x + y - 1

    if result == -1:
        print 'No Number'
    else:
        print result
    return result


num = []
num = [int(i) for i in raw_input().split(" ")]
x = num[0]
y = num[1]
step(x, y)
