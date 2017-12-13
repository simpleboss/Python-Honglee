def input():
    return int(raw_input())


def multofn3(n):
    def digits_to_number(digits):
        number = 0
        position = 1
        for i in range(len(digits)):
            number += digits[-i - 1] * position
            position *= 10
        return number

    multiple_3_point = 0
    for digits_1000 in range(1, 4):
        for digits_100 in range(1, 4):
            for digits_10 in range(1, 4):
                for digits_1 in range(1, 4):
                    number = digits_to_number([digits_1000, digits_100, digits_10, digits_1])
                    if number % n == 0:
                        multiple_3_point += 1
                        #print number
    return multiple_3_point


def main():
    n = input()
    print multofn3(n)


main()
