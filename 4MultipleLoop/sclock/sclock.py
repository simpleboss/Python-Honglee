def input():
    return int(raw_input())


def main(n):
    def replace_char_in_str(original_string, position, replacing_char):
        if type(original_string) is not str:
            raise TypeError('original_string is not a string.')
        if type(position) is not int:
            raise TypeError('position is not an integer.')
        if type(replacing_char) is not str:
            raise TypeError('replacing_char is not a string')
        if position < 0 or position >= len(original_string):
            raise ValueError('position is out of range.')
        if len(replacing_char) != 1:
            raise ValueError('replacing_char is not a string consisting of a single character.')
        
        return original_string[:position] + replacing_char + original_string[position + 1:]

    lengths_space = []
    for i in range(n):
        lengths_space.append(0)
    for i in range(n // 2 + 1):
        lengths_space[i] = i
        lengths_space[n - i - 1] = i

    for line_index in range(n):
        length_space = lengths_space[line_index]

        # Build spaces at the head
        count_spaces = length_space
        line = ' ' * count_spaces

        # Add the asterisks segment
        count_asterisks = n - 2 * length_space
        line += '*' * count_asterisks

        # Replace an asterisks with dollar
        line = replace_char_in_str(line, n - line_index - 1, '$')

        print line


n = input()
main(n)
