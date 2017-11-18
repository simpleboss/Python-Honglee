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
            l3 = 1
            while l3 <= 5:
                total = l1*(day_list[0])


    return day_list


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
m = input_list[0]
n = input_list[1]
input_day_list = []
input_day_list = [int(i) for i in raw_input().split(' ')]
k = raw_input()
when(n, input_day_list, k)
