def speed_limit(n):
    total = 0
    start_time = 0
    i = 1

    while i <= n:
        speed, end_time = map(int, input().split(" "))
        total = total + (end_time - start_time) * speed
        start_time = end_time
        i += 1

    print total
    return total


n = input()
speed_limit(n)
