package main

import (
	"bufio"
	"fmt"
	"os"
)

func getFibNums(sum int) int {
	a := 1
	b := 1
	c := a + b

	for sum <= 4000000 {
		if c%2 == 0 {
			sum += c
		}
		a = b
		b = c
		c = a + b
	}

	return sum
}

func main() {
	sum := 0
	fmt.Println("Sum: ", getFibNums(sum))

	fmt.Println("Press 'Enter' to continue...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
}
