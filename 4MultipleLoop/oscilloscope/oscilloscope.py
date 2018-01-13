def input():
    return int(raw_input())


def main(input_v):
    def make_rows(input_v):
        rows = []
        for i in range(2 * input_v + 1):
            rows.append([''])
        return rows

    def line_star_with_following_spaces(row, index, input_v):
        row.append('*')
        for i in range(index - 1):
            row.append(' ')

    def stair_star_with_following_spaces(row, index, input_v):
        if index > 0 and (index <= 2 * input_v - 1):
            row.append('*')
        for i in range(2 * input_v - index - 1):
            row.append(' ')
    
    rows = make_rows(input_v)
    while len(rows[1]) < 61 + input_v:
        for row in rows:
            index = rows.index(row)

            line_star_with_following_spaces(row, index, input_v)
            stair_star_with_following_spaces(row, index, input_v)

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
