# If n is even: n/2
# If n in odd:  3n + 1


def nextCollatz(n):
    # If "n" is even (modulos to 0)
    if (n%2 == 0):
        return int(n/2)
    else:
        return (int((3*n) + 1))


def main():
    # Length of the longest found collatz chain
    chainLen = 0
    longestCollatz = 0

    for i in range(1, 1000000):
        print(i)
        # Flag for checking if we reached 0 (needed because the first sequence starts with a 1)
        isZero = False
        # Temp space to store our current collatz number
        tmp = i
        # Length of the CURRENT collatz chain
        currChainLen = 1

        # While we haven't reached 0,
        while isZero == False:
            # Then we find the next collatz number
            tmp = nextCollatz(tmp)

            # Add 1 to our chain length
            currChainLen += 1

            if tmp == 1:
                isZero = True

        # If we have found a longer chain, we store it and clear the current chain
        if currChainLen > chainLen:
            chainLen = currChainLen
            currChainLen = 0
            longestCollatz = i
        else:
            currChainLen = 0
    
    print("Longest chain found is: " + str(longestCollatz) + " with length of: " + str(chainLen))

        



if __name__ == "__main__":
    main()