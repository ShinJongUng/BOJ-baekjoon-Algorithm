package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Print((n - 1) * (n - 2) * (n - 3) / 6)
}
