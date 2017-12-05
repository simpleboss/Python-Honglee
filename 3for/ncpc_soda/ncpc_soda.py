def soda(empty, require):
    total = 0
    result = 0
    #print 'empty1', empty
    #print 'require', require
    while empty >= require:
        print 'empty', empty
        result += empty / require
        print 'result', result
        total += result
        empty -= result * require
        empty += result
        print 'after empty', empty
        result = 0
    return total


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
empty = input_list[0] + input_list[1]
require = input_list[2]
print soda(empty, require)
