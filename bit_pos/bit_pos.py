num = raw_input()


def binary(num):
    result = []
    index = []
    while num < 1:
        result.append(num % 2)
        num = num // 2
    for i in result:
        if result[i] == 1:
            index.append(i)
        i += 1
    print index
    return index

