def get_main_number(time):
    if time <= 4:
        print '일일이'
    else:
        total = 7
        i = 3
        d = 2 * (i - 1)
        while total + i < time:
            total = total + d
            i += 1
            if total + i < time and total - i > time:
                break
    print 'total', total
    print 'i', i
    print 'd', d
    return total


get_main_number(25)
