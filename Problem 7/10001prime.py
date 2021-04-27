
def checkPrime(num):
    # First we check the number is greater than 1
    if num > 1:
        # Next, we check all numbers between 1 and itself
        # to see if we find any factors
        for i in range(2, num):
            # If the number, modulo i, equals 0...
            if (num % i) == 0:
                # then break the loop, as the number isn't
                # a prime number
                print(str(num) + " is not a prime")
                return 0
        else:
            # Else, return a 1, as the number IS a prime
            print(str(num) + " IS a prime number")
            return 1


def main():
    # Ask the user what prime number they want to find
    primeToFind = int(input("What Prime would you like to find?: "))

    # Two variables to track what numbers we've checked. the first is the
    # number of primes we have found, the second is a counter to generate
    # numbers to check
    primesFound = 0
    count = 1

    # We keep checking numbers until we find the specified prime number
    while primesFound < primeToFind:
        # If the checkPrime function returns a 1, i.e. the checked number IS a
        # prime, we add a one to the primesFound tracker
        if checkPrime(count) == 1:
            primesFound += 1

        # After we check the number, increment the counter
        count += 1

    # Print a formatted result
    print("The " + str(primeToFind) + "th Prime is: " + str(count - 1))


main()
