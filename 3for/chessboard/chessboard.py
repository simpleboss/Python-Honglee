def get_main_number(time):
    if time <= 4:
        if time == 1:
            print '1 1'
        elif time == 2:
            print '1 2'
        elif time == 3:
            print '2 2'
        elif time == 4:
            print '2 3'
    else:
        total = 3
        i = 2
        while total + i - 1 < time:
            d = 2 * i
            total = total + d
            i += 1
            if total + i < time and total - i > time:
                #print 'break'
                break
    #print 'total', total
    #print 'i', i
    #print 'd', d
    if total == time:
        print i, i
    elif i % 2 == 0:
        get_location_of_number_when_even_line(time, total, i)
    else:
        get_location_of_number_when_odd_line(time, total, i)
    return total


def get_location_of_number_when_odd_line(time, total, i):
    if total > time:
        #print 'odd total>time'
        print i, i - (total - time)
    else:
        #print 'odd total<time'
        print i - (time - total), i


def get_location_of_number_when_even_line(time, total, i):
    if total > time:
        #print 'even total>time'
        print i - (total - time), i
    else:
        #print 'even total<time'
        print i, i - (time - total)


get_main_number(input())
