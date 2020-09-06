def is_prime(n):
    if n == 2:
        return True
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True