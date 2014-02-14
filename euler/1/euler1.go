package main

import "fmt"

func main() {
	j := 0;

	for i := 0; i < 1000; i++{
		if i % 3 == 0 || i % 5 == 0{
			j += i;
		}
	}

	fmt.Println(j);
}