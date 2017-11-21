def input():
    input_list = []
    input_list = [int(i) for i in raw_input().split(' ')]
    m = input_list[0]
    n = input_list[1]
    input_days = []
    input_days = [int(i) for i in raw_input().split(' ')]
    sum = int(raw_input())
    return m, n, input_days, sum


def when_is_first_day(n, input_days, sum):
    sum_d = 0
    for d in input_days:
        sum_d += d - input_days[0]
        for day in range(1, 31):
            if n * day + sum_d == sum:
             first_day = day
             return first_day
             break


def when_1231(m, first_day, input_days):
    if m == 1:
        date_to_1231 = 365 - first_day
    elif m == 2:
        date_to_1231 = 334 - first_day
    elif m == 3:
        date_to_1231 = 306 - first_day
    elif m == 4:
        date_to_1231 = 275 - first_day
    elif m == 5:
        date_to_1231 = 245 - first_day
    elif m == 6:
        date_to_1231 = 214 - first_day
    elif m == 7:
        date_to_1231 = 184 - first_day
    elif m == 8:
        date_to_1231 = 153 - first_day
    elif m == 9:
        date_to_1231 = 122 - first_day
    elif m == 10:
        date_to_1231 = 92 - first_day
    elif m == 11:
        date_to_1231 = 61 - first_day
    else:
        date_to_1231 = 31 - first_day
    result = (date_to_1231 + input_days[0]) % 7
    print result
    return result


def main():
    input()
    when_is_first_day(n, input_days, sum)
    when_1231(m, first_day, input_days)


def test_for_when_is_first_day():
    print 'test1 for example'
    assert(when_is_first_day(3, [1, 2, 6], 18) == 4)
    print 'test2 for Nov'
    assert (when_is_first_day(4, [1, 2, 5, 6], 13+14+17+18) == 13)
    print 'test3 for Dec'
    assert (when_is_first_day(5, [0, 1, 4, 5, 6], 24+25+28+29+30) == 24)
    print 'Test Done'

main()