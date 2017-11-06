def speed_limit(n):
    total = 0
    start_time = 0
    i = 1
    speed = []

    while i <= n:
        speed = [int(j) for j in raw_input().split(" ")]
        '''print speed[0]
        print speed[1]'''
        total = total + (speed[1] - start_time) * speed[0]
        start_time = speed[1]
        speed = []
        i += 1

    print total, ' miles'
    return total


n = input()
speed_limit(n)
