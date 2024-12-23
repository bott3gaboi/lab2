def is_prime(number):
    fl = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            fl = False
            break
    print(fl)


is_prime(int(input()))