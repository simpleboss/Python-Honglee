def input():
    pass


def when_is_first_day(n, input_days, sum):
    pass


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
    pass

