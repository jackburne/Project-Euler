
def main():
    sum = 0
    getFibNumbers(sum)


def getFibNumbers(sum):
    a = 1
    b = 1
    c = a + b
    while sum <= 4000000:
        if (c % 2) == 0:
            sum += c

        a = b
        b = c
        c = a + b

    print(str(sum))


def isFibEven(sum, isEven):
    if (isEven % 2) == 0:
        sum += isEven
        input("c is even")
        return(sum)

    input("c is NOT even")


main()
