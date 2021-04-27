package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


func findLargestPal(numA int, numB int, largestProduct int) {
	// We first loop over the length of Number A (after converting it to a string)
	for len(strconv.Itoa(numA)) {
		// We loop over each character in Number B...
		for len(strconv.Itoa(numB)) {
			// We multiple them together
			palTest := numA * numB

			numPartA, numPartB := 
		}
	}
}

func main() {
	numA := 100
	numB := 100

	fmt.Printf(findLargestPal(numA, numB, 0))
	bufio.NewReader(os.Stdin).ReadBytes('\n')
}
