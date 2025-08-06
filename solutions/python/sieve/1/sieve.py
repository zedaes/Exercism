def primes(limit):
    return [number for number in range(2, limit + 1) if is_prime(number)]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        
    return True
