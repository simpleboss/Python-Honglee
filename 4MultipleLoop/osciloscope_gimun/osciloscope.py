def input():
    return 4

def print_first_chunk(amplitude):
    for y in range(amplitude + 1):
        print y

def main():
    pass

def test(n):
    print_first_chunk(n)

if __name__ == '__main__':
    # main()
    n = input()
    test(n)