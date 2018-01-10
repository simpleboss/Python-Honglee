def input():
    return int(raw_input())


def main(n):
    lengths_space = [0] * n # Create a list which has length of n
    for i in range(n // 2 + 1):
        lengths_space[i] = i
        lengths_space[n - i - 1] = i

    for line_index in range(n):
        length_space = lengths_space[line_index]
        length_asterisks = n - 2 * length_space

        line = ' ' * length_space + '*' * length_asterisks

        # Replace an asterisks with dollar
        dollar_index = n - line_index - 1
        line = line[:dollar_index] + '$' + line[dollar_index + 1:]

        print line


n = input()
main(n)
