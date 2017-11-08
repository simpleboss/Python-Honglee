def count(num):
    total = 0
    i = 1
    #find *th diagonal
    while total < num:
        total = total + i
        i += 1
    #print 'total =', total
    i = i - 1
    #print 'i th diagonal =', i

    #check first number of i th diagonal is odd or even
    if i % 2 == 0:
        #print 'upper if'
        denominator = i + (num - total)
        numerator = 1 - (num - total)
    else:
        #print 'else if'
        denominator = 1 - (num - total)
        numerator = i + (num - total)
    print(str(num) + " IS " + str(denominator) + "/" + str(numerator))
    return total


count(input())
