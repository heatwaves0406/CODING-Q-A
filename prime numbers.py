n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    print(num, ":", is_prime)