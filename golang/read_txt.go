package main

import (
	"fmt"
	"os"
	"io/ioutil"
)

func main() {
	if len(os.Args) < {
		fmt.Println("Usage : " + os.Args[0] + " file name")
		os.Exit(1)
	}

	file, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Cannot read the file")
		os.Exit(1)
	}

	fmt.Print(string(file))
}


