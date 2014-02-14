package main

import "fmt"

func fib(n int) int {
	var result int
	if n < 2 {
		result = 1
	} else {
		result = fib(n-2) + fib(n-1)
	}
	return result
}

func main(){
	i := 0
	sum := 0
	max := 4000000
	for{
		fib := fib(i)
		
		if fib > max{
			break
		}

		if fib % 2 == 0{
			sum += fib
		}
		i++
	}
	fmt.Println(sum)
}