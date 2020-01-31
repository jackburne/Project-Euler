
def findFactor(numToFactor, currDivisor, largestDivisor):
    numFactor = numToFactor
    # A while loop to check that the current divisor we are using is less than
    # or equal to the number we are tryin to find the largest factor for
    while currDivisor <= numToFactor:
        # we divide the number we want to find the largest factor of by the
        # current divisor. If it DOES NOT equal zero, then we increment the
        # current divisor and try again
        while (numToFactor % currDivisor) != 0:

            # print(str(currDivisor) + " does NOT divide into " + str(numToFactor))

            # print("---------PRE IF STATEMENT-----------")
            # print("Number to factor: " + str(numToFactor))
            # print("Current Divisor: " + str(currDivisor))
            # print("Largest Divisor: " + str(largestDivisor))
            # input("Press Enter to contine...")

            # Incrementing the current Divisor by 1
            currDivisor += 1

        # Once we have found a factor for the Number we are finding the largest
        # factor of, we check to see if it is larger than the currently stored
        # largest factor
        if (currDivisor >= largestDivisor):
            # If it is, we then replace the largest current divsor with our
            # current divisor
            largestDivisor = currDivisor
            # We then create a new number to factor by dividng it by the
            # current divisor
            numToFactor = numToFactor / currDivisor
            # Lastly, we reset the current divisor to 2
            currDivisor = 2
        else:
            break

        # print("========POST IF STATEMENT========")
        # print("Number to factor: " + str(numToFactor))
        # print("Current Divisor: " + str(currDivisor))
        # print("Largest Divisor: " + str(largestDivisor))
        # input("Press Enter to contine...")

        continue

    print("Largest possible prime for " + str(numFactor) + " is: " + str(largestDivisor))


def main():
    # Basic set up of variables to find the largest possible divisor
    numToFactor = 600851475143
    currDivisor = 2
    largestDivisor = 0

    findFactor(numToFactor, currDivisor, largestDivisor)


main()
