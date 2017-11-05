test = input()


def parking(number_store):
    i = 1
    location_store = []
    while i <= number_store:
        location = input()
        location_store.append(location)
        i += 1

    min_location = min(location_store)
    max_location = max(location_store)
    print max_location - min_location
    return max_location - min_location


parking(test)
