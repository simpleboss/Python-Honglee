def weeknumber(n, input_day_list, k):
    # get relative date based on input_day_list[0]
    day_list = []
    for i in input_day_list:
        day_list.append(i - input_day_list[0])
    print k
    # find which i is equal to input_day_list[0]
    i = 0
    total = 0
    while i <= 5:
        if total != k:
            total = 0
            for j in day_list:
                total += j * i
        else:
            print 'i', i
            print 'break'
            break
        print 'total', total
        i += 1
    line = i - 2
    return line


def when_input_first_day(day_list, line, k):
    total_difference = 0
    for i in day_list:
        total_difference += i
    while i <= 31:
        if n * i + total_difference == k:
            break
        else:
            i += 1
    day1 = i
    print 'day1', day1
    return day1


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
m = input_list[0]
n = input_list[1]
input_day_list = []
input_day_list = [int(i) for i in raw_input().split(' ')]
k = int(raw_input())
weeknumber(n, input_day_list, k)
when_input_first_day(day_list, line, k)
