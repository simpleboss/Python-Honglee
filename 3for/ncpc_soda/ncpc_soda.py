def soda(empty, require):
    total = 0
    result = 0
    while empty >= require:
        result += empty / require
        total += result
        empty -= result * require
        result = 0
    return total


input = []
input = [int(i) for i in raw_input().split(' ')]
empty = input(0)
require = input(1)
print soda(empty, require)
