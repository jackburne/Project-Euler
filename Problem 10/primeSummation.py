# The sum of primes below 10 is: 2 + 3 + 5 + 7 = 17
# Here, we are finding the sums of primes below 2,000,000

# Utilising the Sieve of Eratosthenes for finding Primes
# between 2 and N
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Using this fix/adjustment:
# https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python


def primeSieve(limit):
    # Creating array a to store a list of initially true flags
    # to indicate a prime number
    a = [True] * limit
    # Setting 0 and 1 to false, as they are never prime
    a[0] = a[1] = False
    # array to store primes in
    primes = []

    # We loop over our array a, and track it's numerical position
    # in the list with "i" and the contents in "isprime"
    for (i, isprime) in enumerate(a):
        # If isprime is true...
        if isprime:
            # We grab i from the enumeration
            yield i
            # and loop over all numbers for i^2, i^2+i, i^2+2i, i^2+3i etc.
            # and set them to false
            for n in range(i*i, limit, i):
                a[n] = False
            
            primes.append(i)

    return primes
    

def sumPrimes(primeList):
    total = 0
    for i in primeList:
        total += i
    
    return total


def main():
    results = primeSieve(2000000)
    total = sumPrimes(results)

    print("Sum of Primes is: " + str(total))


main()
