def parking():
    test = input()
    location_store = [int(i) for i in input().split( )]
    min_location = min(location_store)
    max_location = max(location_store)
    print 2 * (max_location - min_location)
    return 2 * (max_location - min_location)


parking()
