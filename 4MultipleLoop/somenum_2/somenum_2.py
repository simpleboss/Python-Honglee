def somenum():
    for i in range(1, 10001):
        integer_nb = pow(i, 0.5) * 100 // 100
        j = 1
        while j <= integer_nb:
            if i % j != 0:
                break
            j += 1
        if j - 1 == integer_nb:
            print i


somenum()