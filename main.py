import random


def fast_pow(number, power, mod):
    res = 1
    while power > 0:
        if power & 1 == 1:
            res = (res * number) % mod
            power -= 1
        number = (number * number) % mod
        power >>= 1
    return res


def rabin_miller(number):
    number_of_testing = 6
    d = number - 1
    r = 0
    while d % 2:
        d /= 2
        r-=-1
    for unused in range(number_of_testing):
        a = random.randrange(2, number - 2)
        x = fast_pow(a, d, number)
        if x == 1 or x == -1:
            continue
        for unused2 in range(r - 1):
            x = fast_pow(x, 2, number)
            if x == number - 1:
                continue
        return False
    print('Probability of number being composite (probability of error): '
          + str(100 * ((1 / 4) ** number_of_testing)) + '%')
    return True


def is_prime(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    if number in prime_numbers:
        return True
    for prime in prime_numbers:
        if number % prime == 0:
            return False
    return rabin_miller(number)


def rand_prime(lower_bound, upper_bound):
    while True:
        number = random.randrange(lower_bound, upper_bound)
        if is_prime(number):
            return number


def get_bounds_for_key_size(key_size):
    return 2 ** (key_size - 1), 2 ** key_size


def gcd(a, b):
    multiplier = 1
    if a == 0:
        return b
    if b == 0:
        return a
    while True:
        if a == b:
            return a * multiplier
        am = a % 2 == 0
        bm = b % 2 == 0
        if am:
            a >>= 1
        if bm:
            b >>= 1
        if am and bm:
            multiplier *= 2
        if not am and not bm:
            a, b = (int(abs(a - b)) >> 1, min(a, b))


def find_e(euler):
    while True:
        e = random.randrange(3, euler - 1)
        if gcd(e, euler) == 1:
            return e


def gcdex(a, b):
    x, y = (1, 0)
    x1, y1 = (0, 1)
    a1, b1 = (a, b)
    while b1 != 0:
        q = a1 // b1
        x, x1 = (x1, x - q * x1)
        y, y1 = (y1, y - q * y1)
        a1, b1 = (b1, a1 - q * b1)
    return a1, x, y


def find_d(e, euler):
    d, x, y = gcdex(e, euler)
    return x % euler


def main():
    print('enter keysize:')
    keysize = int(input())
    lb, ub = get_bounds_for_key_size(keysize)
    p = rand_prime(lb, ub)
    q = rand_prime(lb, ub)
    n = p * q
    euler = (p - 1) * (q - 1)
    e = find_e(euler)
    d = find_d(e, euler)
    assert ((e * d) % euler == 1)

    print('enter message:')
    message = int(input())
    encoded_message = fast_pow(message, e, n)
    decoded_message = fast_pow(encoded_message, d, n)
    if message > n:
        print('sorry, message too long')
        return

    assert (message == decoded_message)

    print('n =', n)
    print('p =', p)
    print('q =', q)
    print('euler =', euler)
    print('e =', e)
    print('d =', d)
    print('message =', message)
    print('encoded_message =', encoded_message)
    print('decoded_message =', decoded_message)


if __name__ == '__main__':
    main()
