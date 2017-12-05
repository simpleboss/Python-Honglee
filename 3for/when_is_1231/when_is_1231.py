def weeknumber(n, input_day_list, k):
    # get relative date based on input_day_list[0]
    day_list = []
    for i in input_day_list:
        day_list.append(i - input_day_list[0])
    #print k
    # find which i is equal to input_day_list[0]
    i = 0
    total = 0
    while i <= 5:
        if total != k:
            total = 0
            for j in day_list:
                total += j * i
        else:
            break
        i += 1
    line = i - 2
    #print 'line', line
    when_input_first_day(day_list, line, k)
    return line, day_list


def when_input_first_day(day_list, line, k):
    total_difference = 0
    for i in day_list:
        total_difference += i
    #print 'total_difference = ', total_difference
    i = 0
    while i <= 31:
        if n * i + total_difference == k:
            break
        else:
            i += 1
    day1 = i
    #print 'day1', day1
    when_is_1231(m, day1)
    return day1

def when_is_1231(m, day1):
    if m == 1:
        date_to_1231 = 365 - day1
    elif m == 2:
        date_to_1231 = 334 - day1
    elif m == 3:
        date_to_1231 = 306 - day1
    elif m == 4:
        date_to_1231 = 275 - day1
    elif m == 5:
        date_to_1231 = 245 - day1
    elif m == 6:
        date_to_1231 = 214 - day1
    elif m == 7:
        date_to_1231 = 184 - day1
    elif m == 8:
        date_to_1231 = 153 - day1
    elif m == 9:
        date_to_1231 = 122 - day1
    elif m == 10:
        date_to_1231 = 92 - day1
    elif m == 11:
        date_to_1231 = 61 - day1
    else:
        date_to_1231 = 31 - day1
    result = (date_to_1231 + input_day_list[0]) % 7
    print result
    return result


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
m = input_list[0]
n = input_list[1]
input_day_list = []
input_day_list = [int(i) for i in raw_input().split(' ')]
k = int(raw_input())
weeknumber(n, input_day_list, k)
