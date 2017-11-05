test = input()


def parking(number_store):
    i = 1
    location_store = []
    while i <= number_store:
        location = input()
        location_store.append(location)
        i += 1
    min = min(location_store)
    max = max(location_store)
    print max - min
    return max - min

parking(test)