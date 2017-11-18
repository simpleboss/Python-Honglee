def when(n, input_day_list, k):
    # get relative date based on input_day_list[0]
    day_list = []
    for i in input_day_list:
        day_list.append(i - input_day_list[0])
    print day_list
    # find input_day_list[0]
    l1 = 1
    while i <= 5:
        l2 = 1
        while l2 <= 5:
            if len(input_day_list) >= 3:
                l3 = 1
                while l3 <= 5:
                    if len(input_day_list) >= 4:
                        l4 = 1
                        while l4 <= 5:
                            l4 += 1
                            if len(input_day_list) >= 5:
                                l5 = 1
                                while l5 <= 5:
                                    l5 += 1
                                    if len(input_day_list) >= 6:
                                        l6 = 1
                                        while l6 <= 5:
                                            l6 += 1
                                            if len(input_day_list) >= 7:
                                                l7 = 1
                                                while l7 <= 5:
                                                    l7 += 1


    return day_list


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
m = input_list[0]
n = input_list[1]
input_day_list = []
input_day_list = [int(i) for i in raw_input().split(' ')]
k = raw_input()
when(n, input_day_list, k)
