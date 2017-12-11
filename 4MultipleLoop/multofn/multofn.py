def input():
    return int(raw_input())


def multofn(n):
    nominate_list = []
    answer = 0
    for i in range(1111, 3334):
        if i % n == 0:
            nominate_list.append(i)

    nominates_digits = []
    for i in range(len(nominate_list)):
        nominates_digits.append([])
        nominates_digits[i].append((nominate_list[i] // 1000) % 10)
        nominates_digits[i].append((nominate_list[i] // 100) % 10)
        nominates_digits[i].append((nominate_list[i] // 10) % 10)
        nominates_digits[i].append((nominate_list[i] // 1) % 10)
        
    for i in range(len(nominates_digits)):
        for nominates_digit in nominates_digits[i]:
            for digit_123 in range(1, 4):
                if nominates_digit == digit_123:
                    nominates_digits[i].append('ok')
                    break

    answer_count = 0
    for i in range(len(nominates_digits)):
        is_all_ok = True
        for j in range(4):
            if nominates_digits[i][-j - 1] != 'ok':
                is_all_ok = False
        if is_all_ok:
            answer_count += 1
    print answer_count


def main():
    n = input()
    #n = 3
    multofn(n)


main()
