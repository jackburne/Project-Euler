
def smallestDivisors(x):
    checklist = [11, 13, 14, 16, 17, 18, 19, 20]

    # Using xrange in a for loop that starts at 2520 and each iteration is a
    # jump of 20
    for i in range(x, 999999999, x):
        # Check if all the results in this iterated statement are true. This
        # checks if the number, i, is evenly divisible by all numbers in
        # checklist
        if all(i % n == 0 for n in checklist):
            # If it is, we return the answer to main()
            return i


def main():
    # Don't need to start searching until 2520 as any correct number would be
    # more than 2520
    x = 2520

    ans = smallestDivisors(x)
    print(str(ans))


main()
