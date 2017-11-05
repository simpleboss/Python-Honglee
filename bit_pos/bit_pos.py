test = input()


def binary(numbers):
    result = []
    index = []
    while numbers > 0:
        result.append(numbers % 2)
        numbers = numbers // 2

    i = 0
    while i < len(result):
        if result[i] == 1:
            print i,
            '''index.append(i)'''
        i += 1

    return index


binary(test)
