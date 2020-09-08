package main

import "fmt"

func findMulti() int {
	var sum int

	for x := 0; x <= 999; x++ {
		if x%3 == 0 {
			sum += x
			continue
		} else if x%5 == 0 {
			sum += x
			continue
		}
	}

	return sum
}

func main() {
	fmt.Print(findMulti())
}
