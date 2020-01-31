# Finding the multiples of 3 or 5 and creating an array
def findMultiples(sum):
    # checking numbers in the range of 0 to 1000
    for x in range(1000):

        #print("Current Number is: " + str(x))
        #input("Press Enter to continue...")

        # If the remainder after dividing it by 3 is 0, then it is a multiple
        # of 3 and we add it to the sum and go to the next iteration of the
        # loop
        if (x % 3) == 0:
        #    input("Divided by 3 and got 0")
            sum += x
        #    input("Added " + str(x) + " to sum. Sum is now: " + str(sum))
            continue
        # If the remainder after dividing by 5 is 0, then the number is a
        # multiple of 5 and is added to the sum
        elif (x % 5) == 0:
        #    input("Divided by 5 and got 0")
            sum += x
        #    input("Added " + str(x) + " to sum. Sum is now: " + str(sum))
            continue

    print(str(sum))


# Main loop to call the multiple finder
def main():
    findMultiples(0)


main()
