command = input()


prime_sum = 0
non_prime_sum = 0
while command != "stop":
    prime = True
    number = int(command)
    if number < 0:
        print("Number is negative.")
    else:
        for i in range(2, int(number**0.5) + 1):  # range(2, number), just to make it faster
            if number % i == 0:
                prime = False
                break
        if prime:
            prime_sum += number
        else:
            non_prime_sum += number
    command = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
