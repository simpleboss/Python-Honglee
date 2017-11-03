
def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        result = (numbers[len(numbers) / 2 - 1] + numbers[len(numbers) / 2]) // 2
    else:
        result = numbers[(len(numbers) - 1) / 2]
    return result

print("%d" % (median([4, 5, 5, 4])))