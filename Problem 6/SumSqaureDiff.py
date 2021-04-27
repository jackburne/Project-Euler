

# Function for calculating the squares of natural numbers
def sumOfSquares(sumRange):
    y = 0
    for i in range(sumRange):
        x = i + 1
        y = y + (x * x)

    return y
    #print("Result: " + str(y))


# Function for calculating the square of the SUM of the natural numbers
def sqrOfSum(sqrRange):
    # integer var to hold the sum of the numbers
    x = 0
    # FOR loop to iterate over the given range and add them together
    for i in range(sqrRange):
        print(i + 1)
        x = x + (i + 1)

    resOfSqr = x * x
    return resOfSqr


def main():
    sumRange = int(input("Enter highest number to calculate: "))

    resultSumSqr = sqrOfSum(sumRange)
    resultSqrSum = sumOfSquares(sumRange)

    diffResult = resultSumSqr - resultSqrSum
    print("Sum Square Difference: " + str(diffResult))


main()
