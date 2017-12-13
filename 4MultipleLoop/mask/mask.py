def mask():
    nominate_of_a_and_c = []
    for a in range(3, 10):
        for c in range(3, 10):
            #print a, c
            if a + c > 9 and (a + c) % 10 == 2:
                nominate_of_a_and_c.append([a, c])

   # print nominate_of_a_and_c

    for a_and_c in nominate_of_a_and_c:
        a = a_and_c[0]
        c = a_and_c[1]
        digit_2 = c * 110 + a
        for b in range(1, 10):
            digit_1 = a * 100 + b * 10 + c
            digit_3 = 1000 + a * 100 + b * 10 + 2
            if digit_1 + digit_2 == digit_3:
                print digit_1


mask()
