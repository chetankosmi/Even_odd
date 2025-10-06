def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(numbers):
    prime_count = 0

    for n in numbers:
        if is_prime(n):
            prime_count += 1

    print("Prime numbers:", prime_count)


# Example input
numbers = [2, 3, 4, 5, 6, 7, 9, 11, 13, 14]

count_primes(numbers)