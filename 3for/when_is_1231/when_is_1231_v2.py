def input():
    pass


def when_is_first_day(n, input_days, sum):
    sum_d = 0
    for d in input_days:
        sum_d += d - input_days[0]
    for day in range(1, 31):
        if n * day + sum_d == sum:
            first_day = day
            return first_day
        else:
            print 'No answer'


def main():
    pass


def test_for_when_is_first_day(n, input_days, sum):
    print 'test1 for example'
    assert(when_is_first_day(3, [1, 2, 6], 18) == 4)
    print 'test2 for Nov'
    assert (when_is_first_day(4, [1, 2, 6, 7], 13+14+17+18) == 13)
    print 'test3 for Dec'
    assert (when_is_first_day(5, [0, 1, 4, 6, 7], 24+25+28+29+30) == 24)
    print 'Test Done'

