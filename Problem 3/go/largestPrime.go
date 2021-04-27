package main

import (
	"bufio"
	"fmt"
	"os"
)

func findFac(num2fac int, currDiv int, largestDiv int) (int, int) {
	numFac := num2fac

	for currDiv <= num2fac {
		for num2fac%currDiv != 0 {
			currDiv++
		}
		if currDiv >= largestDiv {
			largestDiv = currDiv
			num2fac = num2fac / currDiv
			currDiv = 2
		} else {
			break
		}
		continue
	}
	return numFac, largestDiv
}

func main() {
	num2fac := 600851475143
	currDiv := 2
	largestDiv := 0

	x, y := findFac(num2fac, currDiv, largestDiv)

	fmt.Printf("Largest possible prime for %d is: %d", x, y)

	fmt.Println("Press 'Enter' to continue...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
}
