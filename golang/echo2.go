// echo2 prints its commandline args
package main

import (
	"fmt"
	"os"
)

func main() {
	s, sep := "", ""
	for i, arg := range os.Args[1:] {
		s += i + sep + arg
		sep = " " 
	}

	fmt.Println(s)
}
