def speed_limit(n):
    total = 0
    start_time = 0
    i = 1
    speed2 = []

    while i <= n:
        speed = input()
        speed2.append(speed.split(" "))
        total = total + (speed(1) - start_time) * speed(0)
        start_time = speed(1)
        speed2 = []
        i += 1

    print total
    return total


n = input()
speed_limit(n)
