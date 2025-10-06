def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


# Example input
numbers = [2, 3, 4, 5, 6, 7, 9, 11, 13, 14]

count_even_odd(numbers)
