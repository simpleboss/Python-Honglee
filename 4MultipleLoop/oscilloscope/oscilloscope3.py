def input():
    return raw_input()


def main(v):
    def front_space(i):
        space = ''
        for j in range(i):
            space += ' '
        return space

    def middle_space(i):
        space = ''
        for j in range(v - i):
            space += ' '
        return space

    def loop(i):
        rows = []
        for i in range(2 * v, -1, -1):
            rows.append(front_space(i) + '*' + middle_space(i) + '*')
        return rows

    def tale(i):
        pass

    WIDTH = 29
    a_loop = loop(v)
    for i in range(v, 2 * v + 1, 1):
        row_to_print = ''
        for j in range(WIDTH / len(a_loop[i])):
            row_to_print += a_loop[i]
        row_to_print += a_loop[i][0:(WIDTH - len(row_to_print))]
        print row_to_print


v = 6
main(v)
