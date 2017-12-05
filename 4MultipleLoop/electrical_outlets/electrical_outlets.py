def input():
    n = int(raw_input())
    input_list = []
    for i in range(n):
        i = int(i)
        input_list.append([])
        input_list[i].append([int(i) for i in raw_input().split(' ')])
    input_list.append(n)
    return input_list


def electrical_outlets(input_list):
    n = input_list[-1]
    
    pass


def main():
    input_list = input()
    electrical_outlets(input_list)
    test(input_list)

def test(input_list):
    print 'len(input_list)', len(input_list)
    n = input_list[-1]
    for i in range(n):
        print input_list[i]


main()
