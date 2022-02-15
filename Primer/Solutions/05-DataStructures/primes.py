def get_numbers() :
    numbers = []
    while True:
        num = int(input("Please enter a number [-1 to quit]: "))
        if num == -1:
            break
        numbers.append(num)
    return numbers

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(5, number//2, 2):
        if number % i == 0:
            return False
    return True

def find_primes(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes

def display_numbers(numbers) :
    print("There are %d prime numbers:" % len(numbers))
    for n in numbers:
        print(n)

if __name__ == "__main__":
    numbers = get_numbers()
    primes = find_primes(numbers)
    display_numbers(primes)