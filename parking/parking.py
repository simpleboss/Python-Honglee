test = input()


def parking(number_store):
    i = 1
    location_store = []
    sum_location = 0
    while i <= number_store:
        location = input()
        location_store.append(location)
        sum_location = sum_location + location
        i += 1

    avg_location = sum_location / number_store
    print 'avg_location', avg_location
    print 'location[0]', location_store[0]

    i = 0
    result = 0
    while i < len(location_store):
        result = result + abs(avg_location - location_store[i])
        i += 1

    print result
    return result

parking(test)