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
        row = []
        for i in range(2 * v, -1, -1):
            row.append(front_space(i) + '*' + middle_space(i) + '*')
        return row

    def tale(i):
        pass

    loop = loop(v)
    for i in range(v, 2 * v + 1, 1):
       print loop[i]


v = 6
main(v)
