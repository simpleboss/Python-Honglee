def square(left_num, right_num):
    min_result = 10001
    total_result = 0
    for j in range(left_num, right_num + 1):
        #print 'j = ', j
        i = 1
        while i <= right_num ** 0.5:
            if i * i == j:
                #print 'i = ', i
                total_result = total_result + j
                if min_result >= j:
                    min_result = j
            i += 1
    if min_result == 10001:
        print '-1'
    else:
        print total_result
        print min_result

    return total_result


#num = []
#num = [int(i) for i in raw_input().split(" ")]
left_num = input()
right_num = input()
square(left_num, right_num)


