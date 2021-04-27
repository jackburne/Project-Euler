# A Pythagorean Triplet is a set of 3 natural numbers a < b < c where
#   a^2 + b^2 = c^2
# Here we are finding a triplet where the resulting a, b, and c = 1000
# We want to find the product of abc

# Find Triplets algorithm from StackOverflow:
# https://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets

def findTriplets(searchRange):
    results = []
    for x in range(searchRange):
        x2 = x * x
        y = x + 1
        z = y + 1

        while z <= searchRange:
            z2 = x2 + y * y
            while z * z < z2:
                z = z + 1
            
            if z*z == z2 and z <= searchRange:
                results.append([x, y, z])

            y = y + 1
    
    return results


def find1000(results):
    flag = False
    for i in results:
        x = i[0]
        y = i[1]
        z = i[2]
        if x + y + z == 1000:
            print("Result Found!")
            print("a: " + str(x) + " b: " + str(y) + " c: " + str(z))
            print("Product is: " + str(x*y*z))
            flag = True
    
    else:
        if flag == False:
            print("No Result for abc = 1000")


def main():
    results = findTriplets(1000)
    find1000(results)


main()
