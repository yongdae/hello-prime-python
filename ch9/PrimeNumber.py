NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10

count, number = 0, 2

print("첫 50개의 소수")

while count < NUMBER_OF_PRIMES:
    isPrime = True
    divisor = 2

    while divisor <= number / 2:

        if number % divisor == 0:
            isPrime = False
            break

        divisor += 1

    if isPrime:
        count += 1

        print(format(number, '5d'), end="")

        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()

    number += 1
