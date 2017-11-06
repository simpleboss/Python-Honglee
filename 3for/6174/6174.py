def test(num):
    count = 0
    while num != 6174:
        raw_list = []
        raw_list.append(num % 10000 / 1000)
        raw_list.append(num % 1000 / 100)
        raw_list.append(num % 100 / 10)
        raw_list.append(num % 10)
        sorted_list = sorted(raw_list)
        min_list = sorted_list
        i = 3
        max_list = []
        while i >= 0:
            max_list.append(min_list[i])
            i -= 1
        #print 'max_list = ', max_list
        #print 'min_list = ', min_list
        max_num = max_list[0] * 1000 + max_list[1] * 100 + max_list[2] * 10 + max_list[3]
        min_num = min_list[0] * 1000 + min_list[1] * 100 + min_list[2] * 10 + min_list[3]
        num = max_num - min_num
        count += 1
    return count


print test(input())
