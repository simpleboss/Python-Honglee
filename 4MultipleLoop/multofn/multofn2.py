def input():
    return int(raw_input())


def multofn2(n):
    def digits_to_number(digits):
        position = 1
        number = 0
        for i in range(len(digits)):
            number += digits[-i - 1] * position
            position *= 10
        return number

    digits = []
    for i in range(4):
        digits.append(0)

    multiples_3_point = 0
    for digit_1000 in range(1, 4):
        for digit_100 in range(1, 4):
            for digit_10 in range(1, 4):
                for digit_1 in range(1, 4):
                    number = digits_to_number([digit_1000, digit_100, digit_10, digit_1])

                    if number % n == 0:
                        multiples_3_point += 1
    return multiples_3_point


def main():
    n = input()
    print multofn2(n)


main()
