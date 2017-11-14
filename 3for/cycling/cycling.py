def cycling(n, input_list):
    range = 0
    result = []
    left = input_list[0]
    for right in input_list:
        if right - left > 0:
            range += right - left
        else:
            if range != 0:
                result.append(range)
                range = 0
        left = right
        n += 1
        result = sorted(result)
        #result = reversed(result)
    return result[0]


n = int(raw_input())
input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
print cycling(n, input_list)
