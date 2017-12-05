def input():
    n = int(raw_input())
    input_list = []
    for i in range(n):
        i = int(i)
        input_list.append([int(i) for i in raw_input().split(' ')])
    input_list.append(n)
    return input_list


def electrical_outlets(input_list):
    n = input_list[-1]
    for i in range(n):
        max = 0
        j = 0
        while j <= len(input_list[i]) - 2:
            #print 'input_list', input_list[i][j]
            max += int(input_list[i][j + 1]) - 1
            j += 1
        max += 1
        print max


def main():
    input_list = input()
    electrical_outlets(input_list)
    #test(input_list)


def test(input_list):
    print 'len(input_list)', len(input_list)
    n = input_list[-1]
    for i in range(n):
        print input_list[i]


main()
