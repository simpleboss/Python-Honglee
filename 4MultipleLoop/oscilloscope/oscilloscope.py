def input():
    return int(raw_input())


def main(input_v):
    def make_rows(input_v):
        rows = []
        for i in range(2 * input_v + 1):
            rows.append([''])
        return rows

    def line_star(rows, input_v):
        for i in range(len(rows)):
            rows[i] += '*'

    def space_after_line_star(rows, input_v):
        for i in range(1, len(rows), 1):
            for j in range(i - 1):
                rows[i] += ' '
        return rows

    def stair_star(rows, input_v):
        for i in range(1, len(rows) - 1):
            rows[i] += '*'
        return rows

    def space_after_stair_star(rows, input_v):
        for i in range(len(rows)):
            for j in range(2 * input_v - i - 1):
                rows[i] += ' '
        return rows

    rows = make_rows(input_v)
    current_column = 0
    while current_column < 61 + input_v:
        line_star(rows, input_v)
        space_after_line_star(rows, input_v)
        stair_star(rows, input_v)
        space_after_stair_star(rows, input_v)
        current_column = len(rows[1])

    result = []
    if input_v >= 10:
        high_limit = 20 + input_v - 10
        low_limit = input_v - 10
        for i in range(low_limit, high_limit + 1):
            result.append(rows[i])
    else:
        # high_limit = input_v * 2
        # low_limit = -1
        for i in range(10 - input_v):
            result.append('')
            for j in range(2 * input_v + 60):
                result[-1] += ' '
        for i in range(len(rows)):
            result.append(rows[i])
        for i in range(10 - input_v):
            result.append('')
            for j in range(2 * input_v + 60):
                result[-1] += ' '

    for i in range(20, -1, -1):
        print("".join(str(x) for x in result[i][input_v + 1:61 + input_v]) + '|{:3}V'.format(i-10))

input_v = input()
main(input_v)
