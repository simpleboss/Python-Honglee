def input():
    return 5


def print_first_chunk(amplitude):
    def line(amplitude, y):
        def build_span(len_total, len_left_blanks):
            """Build a span with blanks, star, and blanks.
                len_total -- Total length of the span
                len_left_blanks -- Length of the blanks before the star.

                If len_left_blanks is less than 0, the span will be a 
            """
            span = ''

            # line = ' ' * len_left_blanks + '*' * (len_total - (len_left_blanks + len_right_blanks)) + ' ' * len_right_blanks
            for i in range(len_left_blanks):
                span += ' '
            if len_left_blanks < len_total and len_left_blanks >= 0:
                span += '*'
            for i in range(len_total - max(0, (len_left_blanks + 1))):
                span += ' '

            return span

        line = build_span(amplitude, y) + '*' + build_span((amplitude - 1), y + (amplitude - 1))

        return line

    for y in range(amplitude, -(amplitude + 1), -1):
        print '{}\t'.format(y) + line(amplitude, y)


def main():
    pass


def test(n):
    print_first_chunk(n)


if __name__ == '__main__':
    # main()
    n = input()
    test(n)