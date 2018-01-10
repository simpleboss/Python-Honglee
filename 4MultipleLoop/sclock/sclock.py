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

    for line_index in range(n):
        # Build the asterisks segment
        count_asterisks = n - 2 * line_index
        if count_asterisks < 0:
            count_asterisks = -1 * count_asterisks + 2
        line = '*' * count_asterisks

        # Add spaces at the head
        count_spaces = (n - count_asterisks) / 2
        line = ' ' * count_spaces + line

        # Replace an asterisks with dollar
        line = replace_char_in_str(line, n - line_index - 1, '$')

        print line


n = input()
main(n)
