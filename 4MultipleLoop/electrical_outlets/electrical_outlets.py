def input():
    n = int(raw_input())
    input_list = []
    for i in range(n):
        i = int(i)
        print i
        input_list.append([int(i) for i in raw_input().split(' ')])
        #input_list[i] = []
    return n, input_list


def electrical_outlets(n):
    pass


def main():
    n = input()
    input_list = input()
    electrical_outlets(n, input_list)


def test(input_list):
    print 'test'
    for i in input_list:
        print 'i', i
        print input_list[i]


main()
test()
