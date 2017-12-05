MAX_LINE_LENGTH = 60 # Default MAX_LINE_LENGTH


def input():
    return 4


def print_chunks(amplitude, line_length=MAX_LINE_LENGTH):
    def line(amplitude, y, max_x):
        def build_span(len_total, len_left_blanks):
            """Build a span with blanks, star, and blanks.
                len_total -- Total length of the span
                len_left_blanks -- Length of the blanks before the star.

                If len_left_blanks is less than 0, the span has no left blank.
                If len_left_blanks is larger than len_total, the span has no star and no right blank.
                If len_left_blanks is equal to len_total, the span has no right blanks.
            """
            span = ''

            # line = ' ' * len_left_blanks + '*' * (len_total - (len_left_blanks + len_right_blanks)) + ' ' * len_right_blanks
            for i in range(min(len_total, len_left_blanks)):
                span += ' '
            if len_left_blanks < len_total and len_left_blanks >= 0:
                span += '*'
            for i in range(len_total - max(0, (len_left_blanks + 1))):
                span += ' '

            return span

        def build_element(amplitude, y):
            return build_span(amplitude, y) + '*' + build_span((amplitude - 1), y + (amplitude - 1))

        line = ''

        while len(line) + (amplitude * 2) <= max_x:
            line += build_element(amplitude, y)

        rest = max_x - len(line)
        line += build_element(amplitude, y)[:rest]

        return line

    for y in range(amplitude, -(amplitude + 1), -1):
        print line(amplitude, y, line_length) + '|{:3}V'.format(y)


def main():
    pass


def test(n, line_length):
    print_chunks(n, line_length)


if __name__ == '__main__':
    # main()
    for line_length in range(MAX_LINE_LENGTH):
        n = input()
        print 'line_length = {}'.format(line_length)
        test(n, line_length)