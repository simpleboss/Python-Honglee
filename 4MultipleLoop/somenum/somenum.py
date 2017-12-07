def somenum():
    for i in range(1, 10001):
        count = 0
        k = 1
        while k <= pow(i, 0.5):
            k += 1
        last_nb = k - 1
        j = 1
        while j <= last_nb:
            if i % j != 0:
                break
            j += 1
        if j == last_nb:
            print i


somenum()
