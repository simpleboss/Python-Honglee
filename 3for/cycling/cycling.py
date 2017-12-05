def cycling(n, input_list):
    range = 0
    result = [0]
    left = input_list[0]
    for right in input_list:
        if right - left > 0:
            range += right - left
            #print 'add range', range
        else:
            if range != 0:
                result.append(range)
                #print 'append result', result
                range = 0
        left = right
        n += 1
    if range != 0:
        result.append(range)
        #print 'append result', result
        range = 0
    result = sorted(result)
    return result[-1]


n = int(raw_input())
input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
print cycling(n, input_list)
