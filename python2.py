def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_in_range(start, end):
    prime_list = []
    for num in range(max(start, 2), end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# Input the range
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

if start_range >= end_range or start_range < 0:
    print("Invalid range.")
else:
    primes = generate_primes_in_range(start_range, end_range)
    print("Prime numbers in the specified range:", primes)
