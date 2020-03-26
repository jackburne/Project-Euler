
def findLargestPalindrome(numA, numB, largestPalProduct):
    # Keep testing products until Number A and Number B are no longer 3 digits
    # long
    while len(str(numA)) < 4:
        while len(str(numB)) < 4:
            # Multiplying the Number A and Number B together, to find the
            # product
            palTest = numA * numB

            # Splitting the string into two by incrementing over it using a
            # pair of slicers. This gets us numPartA and numPartB
            numPartA, numPartB = str(palTest)[:int(len(str(palTest))/2)], str(palTest)[int(len(str(palTest))/2):]

            # We reverse Part B
            numPartB = numPartB[::-1]

            # Then we test to see if the two parts are the same. If they are,
            # then we check to see if the new palindrome is larger than the
            # currently stored largest. If it is, we replace it, if not, we
            # just continue onto the next loop
            if numPartA == numPartB:
                if palTest > largestPalProduct:
                    largestPalProduct = palTest

            # Incrementing Number B
            numB += 1

        # Incrementing Number A and resetting Number B
        numA += 1
        numB = 100

    return largestPalProduct


def main():
    numA = 100
    numB = 100

    print(findLargestPalindrome(numA, numB, 0))


main()
