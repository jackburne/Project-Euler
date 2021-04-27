# Python Solution for Project Euler Problem 8
# "Largest Product in a Series"

# Only using the time module for timing how long
# it takes to find the solution
import time

# Main function that actually does the calculation
def calc13(product):
    # Storing the current time to t0 for calculating how long
    # the calculation took
    t0 = time.time()

    # Integer to store the current largest product
    largestProd = 0
    # Variable for holding the current product
    currProd = 1

    # FOR loop that goes over the whole series, minus 13 characters
    for i in range(0, len(product) - 13):

        # Within this, loop over the NEXT 13 characters in the series
        for x in range(13):

            # ####### Only used for debugging purposes to show the current values ######
            #print("###START###")
            #print("Current Index: " + str(i))
            #print("Current x Val: " + str(x))
            #print("Character in product[" + str(x + i) + "]: " + str(product[x + i]))
            #print("Curent x + i: " + str(x + i))
            #print("Current Product: " + str(currProd))
            #print("###END###")
            #print()

            # Adding the next character along to the current product
            currProd = currProd * int(product[x + i])


         # ####### Only used for debugging of the final comparison ######
        #print("########## Product Comparison #############")
        #print("Current Product: " + str(currProd))
        #print("Largest Product: " + str(largestProd))
        #print()
        #print("############Comparison End###########")

        # Checking if the current product is larger,
        if currProd > largestProd:
            # Make the largest product the current product
            largestProd = currProd
            # Reset the current product to 1
            currProd = 1
        else:
            # If our current product is smaller, we also reset it
            currProd = 1
    
    # Once every character set has been checked, we store the current time
    t1 = time.time()
    # Calculate the total time needed to get the solution
    totalTime = t1 - t0
    print("Time Taken: " + str(totalTime))
    # We then return the largest product
    return largestProd


def main():
    product = """73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450"""

#    print("Product: ")
#    print(repr(product))
#    print()
#    product2 = product.replace("\n", "")
#    print("Produc2: ")
#    print(repr(product2))
#    print()
#
#    product3 = ''.join(product2.split())
#    print(product3)

    # Preparing the input data so it's a single continous string
    product = product.replace("\n", "")
    product = ''.join(product.split())

    # Formatting
    print()

    print("The Largest Product is: " + str(calc13(product)))


main()
