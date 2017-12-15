def amstrong():
    def digits_to_number(digits):
        position = 1
        number = 0
        for i in range(len(digits)):
            number += digits[-i - 1] * position
            position *= 10
        return number

    for digits_100 in range(1, 10):
        for digits_10 in range(1, 10):
            for digits_1 in range(1, 10):
                number = digits_to_number([digits_100, digits_10, digits_1])
                if number == pow(digits_100, 3) + pow(digits_10, 3) + pow(digits_1, 3):
                    print number


amstrong()
