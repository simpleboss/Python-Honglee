input_list = []
i = 0
while i >= 0:
    input_list.append(int(raw_input()))
    print input_list[-1]
    if input_list[-1] == 0:
        for j in range(input_list):
            print 'input_list[j]', input_list[j]
            if input_list[j] == 2:
                print 'No Solution!'
            else:
                print input_list[j] -1
        break

