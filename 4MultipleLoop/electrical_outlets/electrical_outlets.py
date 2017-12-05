def input():
    n = raw_input()
    input_list = []
    for i in range(n):
        input_list[i].append(int(i) for i in raw_input().split(' '))
    return n, input_list


def electrical_outlets(n):
    pass


def main():
    n = input(raw_input)
    input_list = input()
    electrical_outlets(n, input_list)


def test(input_list):
    print 'commit gichan.lee2'


main()
test()
