input_list = []
i = 0
while i >= 0:
    input_list.append(raw_input())
    print input_list[-1]
    if input_list[-1] == 0:
        for j in input_list:
            if j == 2:
                print 'No Solution!'
            else:
                print j-1
        break

