MAX_LINE_LENGTH = 60 # Default MAX_LINE_LENGTH
MAX_VOLTAGE = 10 # Default MAX_VOLTAGE


def input():
    n = int(raw_input())
    if n < 1:
        raise ValueError('input amplitude is too small to draw')
    if n >= MAX_LINE_LENGTH:
        raise ValueError('input amplitude is larger than MAX_LINE_LENGTH')
    return n


def build_line(amplitude, y, max_x):
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


def print_chunks(amplitude, line_length=MAX_LINE_LENGTH):
    for y in range(amplitude, -(amplitude + 1), -1):
        print build_line(amplitude, y, line_length) + '|{:3}V'.format(y)


def main(amplitude, line_length):
    def postfix(y):
        return '|{:3}V'.format(y)

    for y in range(MAX_VOLTAGE, amplitude, -1):
        # print ' ' * line_length + postfix(y)
        line = ''
        for i in range(line_length):
            line += ' '
        print line + postfix(y)
    
    for y in range(amplitude, -(amplitude + 1), -1):
        print build_line(amplitude, y, line_length) + postfix(y)
    
    for y in range(-amplitude, -(MAX_VOLTAGE + 1), -1):
        # print ' ' * line_length + postfix(y)
        line = ''
        for i in range(line_length):
            line += ' '
        print line + postfix(y)


def test(amplitude, line_length):
    # print_chunks(n, line_length)
    main(amplitude, line_length)


if __name__ == '__main__':
    n = input()
    main(n, MAX_LINE_LENGTH)
    # for line_length in range(MAX_LINE_LENGTH):
    #     n = input()
    #     print 'line_length = {}'.format(line_length)
    #     test(n, line_length)