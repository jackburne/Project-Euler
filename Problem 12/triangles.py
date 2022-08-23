# 1. Find the next triangle number (adding all the natural numbers)
# 2. find all the factors of this number
# 3. Is it more than 500?
import math
import time

t1 = time.time()

# Function for finding factors of a given number
def factors(n):
    currFactors = 0

    # We look at every number up to our current number, "n"
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        # If it is a factor (if it divides without a remainder), we add 2 to our count
        # As all factors are pairs
        if (n%i == 0):
            currFactors += 2
        else:
            continue
    
    return currFactors


def main():
    y = 1
    for x in range(2, 1000000):
        y += x

        if factors(y) >= 500:
            print(y)
            t2 = time.time()

            print("Time Taken: " + str(t2-t1))
            break


main()