def input():
    return int(raw_input())


def main(input_v):
    def make_row(input_v):
        row = []
        for i in range(2 * input_v + 1):
            row.append([''])
        return row

    def line_star(row, input_v):
        for i in range(len(row)):
            row[i] += '*'

    def space_after_line_star(row, input_v):
        for i in range(1, len(row), 1):
            for j in range(i - 1):
                row[i] += ' '
        return row

    def stair_star(row, input_v):
        for i in range(1, len(row) - 1):
            row[i] += '*'
        return row

    def space_after_stair_star(row, input_v):
        for i in range(len(row)):
            for j in range(2 * input_v - i - 1):
                row[i] += ' '
        return row

    row = make_row(input_v)
    current_column = 0
    while current_column < 61 + input_v:
        line_star(row, input_v)
        space_after_line_star(row, input_v)
        stair_star(row, input_v)
        space_after_stair_star(row, input_v)
        current_column = len(row[1])

    result = []
    if input_v >= 10:
        high_limit = 20 + input_v - 10
        low_limit = input_v - 10
        for i in range(low_limit, high_limit + 1):
            result.append(row[i])
    else:
        # high_limit = input_v * 2
        # low_limit = -1
        for i in range(10 - input_v):
            result.append('')
            for j in range(2 * input_v + 60):
                result[-1] += ' '
        for i in range(len(row)):
            result.append(row[i])
        for i in range(10 - input_v):
            result.append('')
            for j in range(2 * input_v + 60):
                result[-1] += ' '

    for i in range(20, -1, -1):
        print("".join(str(x) for x in result[i][input_v + 1:61 + input_v]) + '|{:3}V'.format(i-10))

input_v = input()
main(input_v)
